class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo = {}

        def die_simulator_starting_at(start: int, n: int):
            if (start, n) in memo:
                return memo[start, n]
            if n == 1:
                memo[start, n] = 1
            else:
                count = 0
                for j in range(1, min(n, rollMax[start] + 1)):
                    for nxt in range(6):
                        if nxt != start or (j == n - 1 and j < rollMax[start]):
                            count = (count + die_simulator_starting_at(nxt, n - j)) % 1000000007
                memo[start, n] = count
            return memo[start, n]
        return sum((die_simulator_starting_at(i, n) for i in range(6))) % 1000000007
