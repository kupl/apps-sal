class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        max_day = right
        
        
        def check(days):
            num = 0
            count = 0
            for i in bloomDay:
                if i <= days:
                    count+=1
                    if count == k:
                        num += 1
                        count = 0
                else:
                    count = 0
            return num >= m
        
        while left < right:
            mid = (left+right)>>1
            if check(mid) == True:
                right = mid
            else:
                left = mid+1
        
        if left == max_day and check(left) != True:
            return -1
        
        return left
