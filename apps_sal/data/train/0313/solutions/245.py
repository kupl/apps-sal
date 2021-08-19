class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if self.feasible(mid, m, k, bloomDay):  # need min number of days
                right = mid - 1
            else:
                left = mid + 1
        return right + 1

    def feasible(self, mid, m, k, bloomDay):
        # all available flowers after mid days of waiting
        # check if it's possible to make m bouquets with the available flowers
        # need m, k adjacent flowers
        adj_flower = 0
        bouquet_num = 0
        for d in bloomDay:
            if d <= mid:
                adj_flower += 1
                if adj_flower == k:
                    bouquet_num += 1
                    adj_flower = 0
            else:
                adj_flower = 0
        return bouquet_num >= m
