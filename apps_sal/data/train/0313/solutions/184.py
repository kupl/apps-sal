class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def feasible_bloom_day(value):
            total_bouquet = 0
            num_flowers = 0

            for bloom in bloomDay:
                # Flower bloomed
                if bloom > value:
                    num_flowers = 0
                else:
                    total_bouquet += (num_flowers + 1) // k
                    num_flowers = (num_flowers + 1) % k

            return total_bouquet >= m

        left, right = 1, max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if feasible_bloom_day(mid):
                right = mid
            else:
                left = mid + 1

        return left
