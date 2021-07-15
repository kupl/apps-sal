class Solution:
    def findLatestStep(self, a: List[int], m: int) -> int:
        n = len(a)
        ans = -1
        d = {}
        ls = [0]*(n+3)
        for ind, i in enumerate(a):
            j,k = i-1, i+1
            ls[i] = 1
            l,r = ls[j], ls[k]
            # while j<n+2 and ls[j] == 1:
            #     l += 1
            #     j += 1
            # while k>0 and ls[k] == 1:
            #     r += 1
            #     k -= 1
            d[l] = d.get(l, 0) - 1
            d[r] = d.get(r, 0) - 1
            d[l+r+1] = d.get(l+r+1, 0) + 1
            ls[i-l] = l+r+1
            ls[i+r] = l+r+1
            # print(l, r, d, ls)
            if m in d and d[m]>0:
                # print(d, a, m, ls)
                ans = ind+1
            
        return ans
            

