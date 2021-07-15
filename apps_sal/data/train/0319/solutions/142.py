from typing import List

class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        suffix_sum = [0]
        for stone in stones[::-1]:
            suffix_sum += suffix_sum[-1] + stone,

        suffix_sum = suffix_sum[::-1][:-1]
        length = len(stones)
        dp = [float('-inf')] * (length - 3) + suffix_sum[-3:]
        for i in range(length - 2, -1, -1):
            dp[i] = max(dp[i], suffix_sum[i] - min(dp[i + j] for j in range(1, 4) if i + j < length))

        alice = dp[0]
        bob = suffix_sum[0] - dp[0]
        return 'Tie' if alice == bob else 'Alice' if alice > bob else 'Bob'
