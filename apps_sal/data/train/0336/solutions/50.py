class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count=[s.count(chr(i)) for i in range(97,123)]
        t_count=[t.count(chr(i)) for i in range(97,123)]
        diff=[t_count[i]-s_count[i] for i in range(26) if t_count[i]-s_count[i]>0]
        sum=0
        for i in range(len(diff)):
            sum=sum+diff[i]
        
        return sum
