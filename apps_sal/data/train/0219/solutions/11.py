class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        sum=0
        ans=0
        d={}
        for i in range(len(hours)):
            sum=sum+1 if hours[i] >8 else sum-1
            if sum>0:
                ans=i+1
            else:
                if sum not in d:
                    d[sum]=i
                if sum-1 in d:
                    ans=max(ans,i-d[sum-1])
        return ans
        
            
                

