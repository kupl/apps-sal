class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def can_make(day):
            bouquet,count = 0,0
            for i in bloomDay:
                if day>=i:
                    count += 1
                else:
                    count = 0
                if count==k:
                    bouquet += 1
                    count = 0
                    if bouquet==m:
                        return True
            return False
        
        left,right = min(bloomDay),max(bloomDay)
        while left<right:
            mid = left + (right-left)//2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1
        return left
