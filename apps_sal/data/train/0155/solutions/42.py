class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        A = arr
        n = len(A)
        # comp = 0
        @lru_cache(None)
        def dp(i):
            # nonlocal comp
            # comp += 1
            count = 0
            for j in range(i-1, i-d-1, -1):
                if j >= 0 and A[j] < A[i]:
                    count = max(count, dp(j))
                else:
                    break
            for j in range(i+1, i+d+1):
                if j < n and A[j] < A[i]:
                    count = max(count, dp(j))
                else:
                    break
            return count + 1
        
        res = 0
        for k in range(n):
            res = max(res, dp(k))
        # print(comp)
        return res
