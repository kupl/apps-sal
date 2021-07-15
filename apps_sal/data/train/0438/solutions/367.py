class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def union(x, y):
            mp[right[y] - left[y] + 1] -= 1
            mp[right[x] - left[x] + 1] -= 1
            ll = left[x]
            rr = right[y]
            left[ll] = left[rr] = ll
            right[rr] = right[ll] = rr
            mp[rr - ll + 1] += 1
            
        res = -1
        mp = Counter()
        n = len(arr)
        left = [-1] * (n + 1)
        right = [-1] * (n + 1)
        for i, a in enumerate(arr):
            mp[1] += 1
            left[a] = right[a] = a
                        
            if a - 1 > 0 and left[a - 1] != -1:
                union(a-1, a)                
            if a + 1 <= n and left[a + 1] != -1:
                union(a, a + 1)
                
            if mp[m] != 0:
                res = i + 1
        return res
            

