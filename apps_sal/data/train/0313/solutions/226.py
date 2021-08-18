class Solution:
    def minDays(self, bloomDay, m, k):

        def max_bouquets(bdays, k, days):
            count = 0
            cursum = 0
            for d in bdays:
                if (d > days):
                    cursum = 0
                else:
                    cursum += 1
                    if cursum == k:
                        count += 1
                        cursum = 0
            return count

        if m * k > len(bloomDay):
            return -1

        bDays = sorted(list(set(sorted(bloomDay)[m * k - 1:])))
        left = 0
        right = len(bDays)
        minDays = -1
        while left < right:
            mid = left + int((right - left) / 2)
            val = bDays[mid]
            if max_bouquets(bloomDay, k, val) >= m:
                minDays = val
                right = mid
            else:
                left = mid + 1
        return minDays
