class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        N = len(coins)
        mem = [[None for i in range(amount + 1)] for j in range(N + 1)]

        def helper(target, i):
            if mem[i][target] != None:
                return mem[i][target]
            if(target == 0):
                return 0

            if(i == N and target > 0):
                return float('inf')

            if(coins[i] > target):
                mem[i][target] = helper(target, i + 1)
            else:
                include = 1 + helper(target - coins[i], i)
                exclude = helper(target, i + 1)
                mem[i][target] = min(include, exclude)

            return mem[i][target]

        ans = (helper(amount, 0))
        return ans if ans != float('inf') else -1
