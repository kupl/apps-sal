class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def check(days):
            i = 0
            bouquet = 0
            count = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= days:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquet += 1
                    count = 0
                if bouquet == m:
                    return True
            return False
        (low, high) = (min(bloomDay), max(bloomDay))
        while low < high:
            mid = low + (high - low) // 2
            possible = check(mid)
            if possible:
                high = mid
            else:
                low = mid + 1
        return low
