class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def is_possible(days) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers >= k:
                        bouquets += 1
                        flowers = 0
                        if bouquets >= m:
                            return True
                else:
                    flowers = 0
            return False
        if len(bloomDay) < m * k:
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            days = left + (right - left) // 2
            if is_possible(days):
                right = days
            else:
                left = days + 1
        return left
