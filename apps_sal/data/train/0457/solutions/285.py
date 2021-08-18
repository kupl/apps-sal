import math
from functools import lru_cache


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1

        stack = [(0, 0)]
        answer = math.inf

        sortedCoins = sorted(coins)
        visited = set()

        while stack:
            (sum, coinCount) = stack.pop()

            if (sum, coinCount) in visited:
                pass
            elif coinCount >= answer:
                pass
            elif sum == amount:
                answer = min(answer, coinCount)
            elif sum > amount:
                pass
            else:

                for c in sortedCoins:
                    if (
                        (sum + c) <= amount and
                        amount < (sum + (c * (answer - coinCount)))
                    ):
                        stack.append((sum + c, coinCount + 1))

            visited.add((sum, coinCount))

        if answer == math.inf:
            return -1
        else:
            return answer
