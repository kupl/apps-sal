class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def helper(D_days):
            n_m = 0
            n_k = 0

            for index, fl in enumerate(bloomDay):
                if fl > D_days:
                    n_k = 0
                else:
                    n_k += 1

                if n_k == k:
                    n_m += 1
                    n_k = 0

            if n_m < m:
                return +1
            else:
                return -1

        def B_search():
            low, high = 0, max(bloomDay) + 1

            while low < high:
                mid = low + (high - low) // 2

                if helper(mid) == +1:
                    low = mid + 1
                else:
                    high = mid

            return low

        return B_search()
