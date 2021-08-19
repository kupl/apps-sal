class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        F = [0] * (N + 1)
        S = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            max_val = -100000000
            for x in range(min(3, N - i)):
                val = sum(stoneValue[i:i + x + 1]) + S[i + x + 1]
                if max_val < val:
                    max_val = val
                    F[i] = val
                    S[i] = F[i + x + 1]
        if F[0] == S[0]:
            return 'Tie'
        return 'Alice' if F[0] > S[0] else 'Bob'
