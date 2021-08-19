INF = 1 << 60


class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        overlap = [[0] * n for _ in range(n)]
        for (i, j) in product(range(n), repeat=2):
            l = min(len(A[i]), len(A[j]))
            overlap[i][j] = max((k for k in range(l + 1) if A[i][len(A[i]) - k:] == A[j][:k]))
        dp = [[INF] * n for _ in range(1 << n)]
        prev = [[(None, None)] * n for _ in range(1 << n)]
        for (i, S) in enumerate(A):
            dp[1 << i][i] = len(S)
        for (U, i) in product(range(1 << n), range(n)):
            if not U >> i & 1:
                continue
            for ni in range(n):
                if U >> ni & 1:
                    continue
                if dp[U | 1 << ni][ni] > dp[U][i] + len(A[ni]) - overlap[i][ni]:
                    dp[U | 1 << ni][ni] = dp[U][i] + len(A[ni]) - overlap[i][ni]
                    prev[U | 1 << ni][ni] = (U, i)
        (U, i) = ((1 << n) - 1, min(range(n), key=lambda i: dp[-1][i]))
        res = []
        while U is not None:
            res.append(A[i])
            (U, i) = prev[U][i]
        res.reverse()
        ans = ''
        for S in res:
            l = min(len(ans), len(S))
            k = max((k for k in range(l + 1) if ans[len(ans) - k:] == S[:k]))
            ans += S[k:]
        return ans
