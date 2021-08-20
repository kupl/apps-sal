class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        N = len(A)
        cnt = [1 for _ in range(N)]
        for (i, n) in enumerate(A):
            (l, r) = (0, i - 1)
            while r >= l:
                if A[r] * A[l] == n:
                    cnt[i] += cnt[r] * cnt[l] if r == l else cnt[r] * cnt[l] * 2
                    l += 1
                    r -= 1
                elif A[r] * A[l] > n:
                    r -= 1
                else:
                    l += 1
            ans += cnt[i]
        return ans % (10 ** 9 + 7)
