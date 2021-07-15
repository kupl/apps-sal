import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp: List[int] = [0] * (n+1)
        candidates: List[int] = []
        for j in range(1, int(math.sqrt(n))+1):
            candidates.append(j*j)
        for i in range(n):
            if not dp[i]:
                for can in candidates:
                    if i + can < n:
                        dp[i+can] = 1
                    elif i + can == n:
                        return 1
        return dp[-1]
