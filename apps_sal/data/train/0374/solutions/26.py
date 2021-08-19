class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        graph = [[0] * n for _ in range(n)]
        for (i, word1) in enumerate(A):
            for (j, word2) in enumerate(A):
                if i == j:
                    continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break
        memo = {}

        def search(i, k):
            if (i, k) in memo:
                return memo[i, k]
            if i == 1 << k:
                return A[k]
            memo[i, k] = ''
            for j in range(n):
                if j != k and i & 1 << j:
                    candidate = search(i ^ 1 << k, j) + A[k][graph[j][k]:]
                    if memo[i, k] == '' or len(candidate) < len(memo[i, k]):
                        memo[i, k] = candidate
            return memo[i, k]
        res = ''
        for k in range(n):
            candidate = search((1 << n) - 1, k)
            if res == '' or len(candidate) < len(res):
                res = candidate
        return res
