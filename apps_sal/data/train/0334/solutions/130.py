class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        c=0
      
        for i in range(len(s)):
            if i-1>=0 and s[i-1]==s[i]:
                continue
            k=i
            while k<len(s) and s[k]==s[i]:
                k+=1
            if k>i+1:
                print(i)
                a=sum(cost[i:k])-max(cost[i:k])
                c+=a
        return c
