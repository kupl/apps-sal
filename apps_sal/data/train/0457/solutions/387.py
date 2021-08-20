class Solution:

    def coinChange(self, coins: List[int], a: int) -> int:
        l = len(coins)
        mem = []
        for i in range(l + 1):
            mem.append([0] * (a + 1))
            for j in range(a + 1):
                if i == 0:
                    mem[i][j] = float('inf')
                if j == 0:
                    mem[i][j] = 0
                if i > 0 and j > 0:
                    if coins[i - 1] <= j:
                        mem[i][j] = min(1 + mem[i][j - coins[i - 1]], mem[i - 1][j])
                    else:
                        mem[i][j] = mem[i - 1][j]
        if mem[l][a] == float('inf'):
            return -1
        return mem[l][a]
