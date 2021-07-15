class Solution:
    def knightDialer(self, N: int) -> int:
        arr = [1]*10
        mul = [[0,0,0,0,1,0,1,0,0,0],
               [0,0,0,0,0,0,1,0,1,0],
               [0,0,0,0,0,0,0,1,0,1],
               [0,0,0,0,1,0,0,0,1,0],
               [1,0,0,1,0,0,0,0,0,1],
               [0,0,0,0,0,0,0,0,0,0],
               [1,1,0,0,0,0,0,1,0,0],
               [0,0,1,0,0,0,1,0,0,0],
               [0,1,0,1,0,0,0,0,0,0],
               [0,0,1,0,1,0,0,0,0,0]]
        for n in range(N-1):
            newarr = [0]*10
            for i in range(10):
                for j in range(10):
                    newarr[i] += mul[i][j]*arr[j]
                    newarr[i] %= 10**9+7
            arr = newarr
        s = 0
        for x in arr:
            s = (s+x)%(10**9+7)
        return s
