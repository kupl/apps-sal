class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], work: List[int]) -> int:
        maxd = max(d)
        cmb1 = defaultdict(int)
        for i in range(len(p)):
            cmb1[d[i]] = max(cmb1[d[i]], p[i])
        
        cmb = sorted(cmb1.items(), key=lambda x: x[0])

        NN = len(cmb)
        dd = [0]*(maxd+1)
        val = j = 0
        for i in range(maxd+1):
            if j<NN and i == cmb[j][0]:
                val = max(val, cmb[j][1])
                j += 1
            dd[i] = val 
         
        
        ans = 0
        for w in work:
            if w>maxd:
                ans += dd[maxd]
            else:
                ans += dd[w]
        
        return ans
