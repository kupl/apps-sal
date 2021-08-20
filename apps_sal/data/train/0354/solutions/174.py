class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def solve(i, numConsecutive, last):
            if i == n:
                return 1
            if (i, numConsecutive, last) in memo:
                return memo[i, numConsecutive, last]
            count = 0
            for f in range(6):
                if last != f:
                    count += solve(i + 1, 1, f)
                elif numConsecutive + 1 <= rollMax[f]:
                    count += solve(i + 1, numConsecutive + 1, last)
            count %= MOD
            memo[i, numConsecutive, last] = count
            return count
        MOD = 10 ** 9 + 7
        memo = {}
        return solve(0, 0, -1)
