class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=0
        for curr in s:
            # print(\"Curr=\",curr,\"and t=\",t)
            if curr in t:
                t=t.replace(curr,'',1) 
                # print(\"Now t=\",t)
            else:
                count+=1
        return count
