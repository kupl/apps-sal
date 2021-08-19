class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # This is a greedy approach and is generally O(N) time
        def is_feasible(max_day) -> bool:
            total_bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > max_day:
                    flowers = 0
                else:
                    total_bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return total_bouquets >= m

        if m * k > len(bloomDay):
            return -1

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if is_feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l
