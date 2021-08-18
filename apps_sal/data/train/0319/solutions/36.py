class Solution:

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
