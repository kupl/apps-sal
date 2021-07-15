class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        mp={0:1} 
        ans={} 
        for a in A:
            temp={} 
            for m in mp:
                temp[m|a]=1 
            temp[a]=1 
            for t in temp:
                ans[t]=1 
            mp={} 
            for t in temp:
                mp[t]=1 
        cnt=0 
        for c in ans:
            cnt+=1 
        return cnt
            

