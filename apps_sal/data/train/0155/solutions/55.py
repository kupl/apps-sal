class Solution:
    def maxJumps(self, A: List[int], d: int) -> int:
        n = len(A)

        @lru_cache(None)
        def helper(i):
            ans = 1
            l = max(0, i - d)
            r = min(n - 1, i + d)

            for j in reversed(range(l, i)):
                if(A[j] < A[i]):
                    ans = max(ans, 1 + helper(j))
                else:
                    break
            for j in range(i + 1, r + 1):
                if(A[j] < A[i]):
                    ans = max(ans, 1 + helper(j))
                else:
                    break

            return ans

        ans = max([helper(i) for i in range(n)])
        return ans
