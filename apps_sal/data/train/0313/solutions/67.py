class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def condition(cap):
            curr_m = 0
            curr_k = 0
            for flower in bloomDay:
                if flower <= cap:
                    curr_k += 1
                    if curr_k == k:
                        curr_m += 1
                        curr_k = 0
                    if curr_m >= m:
                        return True
                else:
                    curr_k = 0
            return False
        (left, right) = (1, max(bloomDay))
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
