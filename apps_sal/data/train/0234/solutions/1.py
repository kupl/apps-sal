class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res,need=0,0
        for i in range(len(S)):
            if S[i]=='(':
                need+=1
            if S[i]==')':
                need-=1
                if need==-1:
                    need=0
                    res+=1
        return res+need

