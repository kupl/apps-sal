class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def feasible(days):
            flower = 0
            bouq = 0
            # print('----------'+str(days))
            for bloom in bloomDay:
                if bloom > days:
                    flower = 0
                else:
                    flower += 1
                    # print(bloom,flower)
                    if flower >= k:
                        bouq += 1
                        flower = 0
                        # print(bloom,bouq)
            return bouq >= m

        left = 1
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
