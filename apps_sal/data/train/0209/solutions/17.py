class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if (len(stones) - 1) % (K - 1) != 0:
            return -1
        
        presum = 0
        presum_list = [presum]
        for cost in stones:
            presum += cost
            presum_list.append(presum)
        
        # dp[i][j][k]: cost that merges into k piles: from ith pile to jth pile
        n = len(stones)
        dp = [[[math.inf] * (K + 1) for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i][1] = 0
        
        for pile_length in range(1, n + 1):
            # pile_length = j - i + 1
            for i in range(n - pile_length + 1):
                j = pile_length + i - 1
                for possible_k in range(2, min(pile_length, K) + 1):
                    for t in range(i, j):
                        dp[i][j][possible_k] = min(dp[i][j][possible_k], dp[i][t][possible_k - 1] + dp[t + 1][j][1])
                dp[i][j][1] = min(dp[i][j][1], dp[i][j][K] + presum_list[j + 1] - presum_list[i])
        
        return dp[0][n - 1][1]
