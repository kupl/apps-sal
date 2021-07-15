class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_list=Counter(s)
        count=0
        for i in range(len(t)):
            if (t[i] in s_list) and s_list[t[i]]>0:
                s_list[t[i]]-=1
            else:
                count+=1
        return count
