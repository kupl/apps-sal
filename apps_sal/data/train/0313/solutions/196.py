class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        low = 0
        high = max(bloomDay)

        if m * k > len(bloomDay):
            return -1

        def can_make_bouquets(mid):
            days = 0
            curr = [0] * len(bloomDay)
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    if i == 0:
                        curr[i] = 1
                    elif curr[i - 1] == k:
                        curr[i] = 1
                    else:
                        curr[i] = curr[i - 1] + 1

            if curr.count(k) >= m:
                return True

            return False

        while low < high:
            mid = math.floor((low + high) / 2)
            if can_make_bouquets(mid):
                high = mid
            else:
                low = mid + 1

        return low
