class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.dp(s,0,0,[])
        
    def dp(self,s,start,pos,ans):
        if pos == len(s):
            return len(ans)
        a = 0
        b = self.dp(s,start,pos+1,list(ans))
        if s[start:pos+1] not in ans:
            ans.append(s[start:pos+1])
            a = self.dp(s,pos+1,pos+1,list(ans))
            ans.pop()
        # ans.remove(s[start:pos+1])
        
        return a if a > b else b
        # return ans

