class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m>n: return -1
        if m==n: return n
        helper = [0]*(n+1)
        res = -1
        
        for k, i in enumerate(arr):
            helper[i] = l = r = i
            if l>1 and helper[l-1]:
                l = helper[l-1]
                if r - l == m:
                    res = k
                helper[l], helper[r] = r, l
            if r<n and helper[r+1]:
                r = helper[r+1]
                if r - i == m:
                    res = k
                helper[l], helper[r] = r, l
                
        return res
