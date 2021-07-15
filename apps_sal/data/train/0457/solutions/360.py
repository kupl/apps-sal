class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:

        table = [[float('inf') for _ in range(target+1)] for _ in range(len(coins)+1)]
    
        for i in range(len(coins)+1):
            table[i][0] = 0
        for i in range(1, len(coins)+1):
            for j in range(target+1):
                if coins[i-1] <= j:
                    a = 1 + table[i][j-coins[i-1]]
                else:
                    a = float('inf')
                b = table[i-1][j]
                if a <= b:
                    table[i][j] = a
                
                else:
                    table[i][j] = b
        return table[-1][-1] if table[-1][-1] != float('inf') else -1
