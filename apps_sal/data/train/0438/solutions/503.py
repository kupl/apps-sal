class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        p = list(range(n))
        size = [0]*n

        def find(x):
            if x!=p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x,y):
            px,py = find(x),find(y)
            if px == py:
                return False
            if size[px]>size[py]:
                p[py] = px
                size[px]+=size[py]
            else:
                p[px] =py
                size[py] += size[px]
            return True

        if m == len(arr):
            return m
        ans = -1
        for step,i in enumerate(arr):
            i -= 1
            
            for j in range(i-1,i+2):
                if 0<=j<n:
                    if size[find(j)]==m:
                        ans = step
            size[i] = 1
            for j in range(i-1,i+2):
                if 0<=j<n:
                    if size[j]:
                        union(i,j)
        return ans
    
    # 4 1 3
    # 4 5 8

