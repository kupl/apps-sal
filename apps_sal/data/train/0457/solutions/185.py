class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i][j] first j coins with sum of i
        # dp[i][j] = min(dp[j-coins[k][k]]+1) for k in coins
        
        n = len(coins)
        dp = [0] + [float('inf')] * amount
        for j in range(1, amount+1):
            for i in range(n):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[-1] if dp[-1] < float('inf') else -1
'''
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int Max = amount + 1;
        vector<int> dp(amount + 1, Max);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.size(); j++) {
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};
'''
