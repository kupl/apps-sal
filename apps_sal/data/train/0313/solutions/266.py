class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n//k < m:
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)
        
        while left < right:
            mid = (left + right)//2
            numBouqets = 0
            count = 0
            for i in range(n):
                if bloomDay[i]<=mid:
                    count += 1
                else:
                    count = 0
                if count == k:
                    count = 0
                    numBouqets += 1
            # print(left, mid, right, numBouqets)
            if numBouqets >= m:
                right = mid
            else:
                left = mid+1
        return left
