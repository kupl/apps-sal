class Solution:

    def minDays(self, bloomDay: List[int], num_bouq: int, num_flowers: int) -> int:

        def canMake(day):
            i = 0
            num_adj = 0
            count = 0
            while i < len(bloomDay):
                if bloomDay[i] <= day:
                    num_adj += 1
                if num_adj == num_flowers:
                    count += 1
                    num_adj = 0
                if bloomDay[i] > day:
                    num_adj = 0
                i += 1
            return count >= num_bouq
        left = 1
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if canMake(mid):
                right = mid
            else:
                left = mid + 1
        if canMake(left):
            return left
        else:
            return -1
