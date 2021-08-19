class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        lower_bound = min(bloomDay)
        upper_bound = max(bloomDay)
        while lower_bound < upper_bound:
            days = (lower_bound + upper_bound) // 2
            if self.can_make_bouquets(bloomDay, m, k, days):
                upper_bound = days
            else:
                lower_bound = days + 1
        return upper_bound

    def can_make_bouquets(self, bloomDay, m, k, days):
        bouquets_made = 0
        adj_count = 0
        K = k
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                K -= 1
            else:
                K = k
            if K == 0:
                bouquets_made += 1
                K = k
        return bouquets_made >= m
