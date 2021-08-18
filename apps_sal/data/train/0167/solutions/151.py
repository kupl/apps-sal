class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        @lru_cache(None)
        def helper(floors, eggs):
            if floors <= 0:
                return 0
            if eggs == 1:
                return floors
            ans = floors
            low, high = 1, floors
            while low + 1 < high:
                mid = low + (high - low) // 2
                t1 = helper(mid - 1, eggs - 1)
                t2 = helper(floors - mid, eggs)
                if t1 < t2:
                    low = mid
                elif t1 > t2:
                    high = mid
                else:
                    low = high = mid
            ans = floors
            for k in (low, high):
                ans = min(ans, 1 + max(helper(k - 1, eggs - 1), helper(floors - k, eggs)))

            return ans
        return helper(N, K)
