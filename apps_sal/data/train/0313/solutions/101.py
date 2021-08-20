class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        r = max(bloomDay)
        ans = -1
        while l <= r:
            mid = l + r >> 1
            adjs = 0
            bouqs = 0
            for day in bloomDay:
                if day <= mid:
                    adjs += 1
                else:
                    bouqs += adjs // k
                    if bouqs >= m:
                        break
                    adjs = 0
            bouqs += adjs // k
            if bouqs >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
