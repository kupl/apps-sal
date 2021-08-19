class Solution:
    # Time: O(n * k), Space: O(n) - where k is number of maximum stones a player can pick
    def bottomUpDP(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        suffix_sum = [0 for _ in range(n + 1)]
        # dp[i] - maximum sum a player can accumulate he/she starts at position i
        dp = [0 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            suffix_sum[i] = stoneValue[i] + suffix_sum[i + 1]

        for i in range(n - 1, -1, -1):
            player_pick_two_stones, player_pick_three_stones = float('-inf'), float('-inf')
            player_pick_one_stone = stoneValue[i] + suffix_sum[i + 1] - dp[i + 1]
            if i + 1 < n:
                player_pick_two_stones = stoneValue[i] + stoneValue[i + 1] + suffix_sum[i + 2] - dp[i + 2]
            if i + 2 < n:
                player_pick_three_stones = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + suffix_sum[i + 3] - dp[i + 3]
            dp[i] = max(player_pick_one_stone, player_pick_two_stones, player_pick_three_stones)

        if 2 * dp[0] == suffix_sum[0]:
            return 'Tie'
        elif 2 * dp[0] > suffix_sum[0]:  # Alice score > Bob's score, dp[0] > suffix_sum[0] - dp[0]
            return 'Alice'
        else:
            return 'Bob'

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        prefix = list(itertools.accumulate(stoneValue))

        @lru_cache(maxsize=None)
        def getScore(i):
            if i > len(stoneValue):
                return 0

            stones = float('-inf')
            for j in range(1, 3 + 1):
                prev = prefix[i - 1] if i - 1 >= 0 else 0
                stones = max(stones, prefix[-1] - prev - getScore(i + j))
            return stones

        alice_score = getScore(0)

        if alice_score > prefix[-1] - alice_score:
            return 'Alice'
        elif alice_score < prefix[-1] - alice_score:
            return 'Bob'
        else:
            return 'Tie'
