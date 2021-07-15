class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for k in arr:
            if k in d:
                d[k] += 1
            else:
                d[k] = 1
                
        t = []
        for k, v in d.items():
            t.append(v)
        t.sort(reverse=True)
        r = 0
        ii = 0
        while r < len(arr)//2 + len(arr)%1 :
            r += t[ii]
            ii+=1
        return ii
