class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay): return -1
        left=min(bloomDay)
        right=max(bloomDay)
        
        while left<right:
            mid=(left+right)//2
            print((left,right,mid,self.boquets(bloomDay,mid,k)))
            if self.boquets(bloomDay,mid,k)>=m:
                right=mid
            else:
                left=mid+1
    
        return left
    def boquets(self,bloom,day,k):
        res=0
        cur=0
        
        for d in bloom:
            if d<=day:
                cur+=1
            else:
                cur=0
            if cur==k:
                res+=1
                cur=0
        return res
        

