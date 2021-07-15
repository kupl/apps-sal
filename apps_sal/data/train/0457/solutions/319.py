import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        arr = coins
        w = amount
        
        n = len(arr)
        t = [[0]*(w+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(w+1):
                if j == 0 and i!=0:
                    t[i][j] = 0
                if i == 1 and j!=0:
                    t[i][j] = int(j/arr[i-1]) if j%arr[i-1] == 0 else math.inf

        for i in range(2, n+1):
            for j in range(1, w+1):
                if arr[i-1] <= j:
                    t[i][j] = min(t[i][j-arr[i-1]]+1, t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        # from pprint import pprint
        # pprint(t)
        return -1 if t[n][w]==math.inf else t[n][w]

