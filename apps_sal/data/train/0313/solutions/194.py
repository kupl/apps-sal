class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # arr[i] = time after which we can use index i, k = no. of adjacent flowers , m = no. of boquet
        # ans = min. no of days to make m boquet else -1
        
        # arr = [1,10,3,4,10,2] m = 3 k = 2
        # ans = 10
        
        # after d will there be m subarrays with k elements each?
        
        def feasible(d) -> bool:
            # m separate subbarr of size k where max val in each subarr <= d
            count = 0
            prevBadIndex = -1
            for i in range(len(bloomDay)):
                if bloomDay[i] > d:
                    count += (i - prevBadIndex - 1) // k
                    prevBadIndex = i
            
            if prevBadIndex != len(bloomDay) - 1:
                count += (len(bloomDay) - prevBadIndex - 1) // k
            
            return count >= m
        
        if len(bloomDay) < (m * k):
            return -1
        
        
        left,right = min(bloomDay), max(bloomDay)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
