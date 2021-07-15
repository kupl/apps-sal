import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = collections.Counter(arr)
        
        vals = sorted(list(d.values()),reverse=True)
        
        ans = 0
        s = 0
        for i in range(len(vals)):
            ans += 1
            s += vals[i]
            if s >= len(arr)//2:
                return ans

