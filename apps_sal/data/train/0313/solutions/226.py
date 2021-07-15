class Solution:
    def minDays(self, bloomDay, m, k):

        #print (f\"bloomDay={bloomDay} m={m} k={k}\")

        def max_bouquets(bdays, k, days):
            count = 0
            cursum = 0
            for d in bdays:
                if (d > days ):
                    cursum = 0 # can't pick up that flower
                else:
                    cursum += 1
                    if cursum == k:
                        count += 1
                        cursum = 0
            #print(f\"bdays={bdays} -> can make {count} bouquets if waiting {days} days\")
            return count

        if m*k > len(bloomDay):
            return -1

        bDays = sorted(list(set(sorted(bloomDay)[m*k-1:])))
        left = 0
        right = len(bDays)
        minDays = -1
        while left<right:
            mid = left + int((right-left)/2)
            #print(f\"left={left} mid={mid} right={right}\")
            val = bDays[mid]
            if max_bouquets(bloomDay,k, val) >= m:
                minDays = val
                right = mid
            else:
                left = mid+1
        return minDays
        

