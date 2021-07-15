class Solution:
    def maxSum(self, arra: List[int], arrb: List[int]) -> int:
        m, n = len(arra), len(arrb)
        dica = {a: i for i, a in enumerate(arra)}
        dicb = {b: i for i, b in enumerate(arrb)}
        dpa, dpb = {}, {}
        
        def go(i, f):
            arr1, arr2 = arra, arrb
            dic1, dic2 = dica, dicb
            dp1, dp2 = dpa, dpb
            if not f:
                arr1, arr2 = arr2, arr1
                dic1, dic2 = dic2, dic1
                dp1, dp2 = dp2, dp1
            a = arr1[i]
            d = a + (dp1[arr1[i-1]] if i > 0 else 0)
            if a in dic2 and dic2[a] > 0:
                d = max(d, a+dp2[arr2[dic2[a]-1]])
            dp1[a] = d
        
        i, j = 0, 0
        while i < m and j < n:
            if arra[i] <= arrb[j]:
                go(i, True)
                i += 1
            else:
                go(j, False)
                j += 1
        
        while i < m:
            go(i, True)
            i += 1
        while j < n:
            go(j, False)
            j += 1
        return max(dpa[arra[-1]], dpb[arrb[-1]]) % (1000000007)

