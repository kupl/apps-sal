class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], X: int) -> int:
        arr = [0]
        n = len(g)
        for i in range(n):
            arr.append(arr[-1]+(1-g[i])*c[i])
        
        c = [0]+c
        for i in range(n):
            c[i+1] = c[i]+c[i+1]
        
        m = -1
        for i in range(X,n+1):
            m = max(m,c[i]-c[i-X]-arr[i]+arr[i-X])
        
        print((arr,c,m))
        
        return arr[-1]+m

