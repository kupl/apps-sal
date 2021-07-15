from collections import OrderedDict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        fq = {}
        for i in arr:
            fq[i] = fq.get(i, 0) + 1
        sorted_m = OrderedDict(sorted(list(fq.items()), key=lambda k:(k[1], k[0]), reverse=True))
        
        sm = 0
        req = len(arr)//2 + len(arr)%2
        ans = 0
        for i in sorted_m:
            sm += sorted_m[i]
            ans += 1
            if sm>=req:
                break
        return ans

