class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        stack,res,first=0,0,{}
        for day,i in enumerate(hours):
            stack=stack+1 if i>8 else stack-1
            first.setdefault(stack, day)
            if stack>0:res=day+1
            elif stack-1 in first:
                res=max(res,day-first[stack-1])
        return res
