class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def feasible(days):
            bouquets=flowers=0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=days:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                    if bouquets>=m:
                        return True
                else:
                    flowers=0
            return False
        if m*k>len(bloomDay):
            return -1
        left,right=min(bloomDay),max(bloomDay)
        while left<right:
            mid=left+(right-left)//2
            if feasible(mid):
                right=mid
            else:
                left=mid+1
        return left
