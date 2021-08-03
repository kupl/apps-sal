

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m * k:
            return -1

        def isPossible(l):
            i = 0
            temp = 0
            num_bouquets = 0
            while i < len(bloomDay):
                if bloomDay[i] > l:
                    temp = 0
                else:
                    temp += 1
                    if temp == k:
                        num_bouquets += 1
                        if num_bouquets == m:
                            return True
                        temp = 0

                i += 1

            return False

        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = low + (high - low) // 2
            if isPossible(mid):
                high = mid
            else:
                low = mid + 1
        return low
