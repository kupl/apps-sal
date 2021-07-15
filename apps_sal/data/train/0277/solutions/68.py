from heapq import heappush,heappop,heapify
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n=len(light)
        a=[]
        ans=0
        for i in range(n):
            heappush(a,-1*(light[i]))
            if len(a)==i+1:
                temp=-1*heappop(a)
                if  temp==i+1:
                    ans+=1
                heappush(a,-1*temp)
        return ans
