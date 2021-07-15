class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # Idea:
        # 1. DP with optimal substructure where:
        #       number of sequences with length N ending at X is sum of:
        #           number of sequences with length N - 1 ending at non-X
        #           number of sequences with length N - 2 ending at non-X
        #           ...
        #           number of sequences with length N - C ending at non-X
        #
        #       where C is number of repeats from which its not allowed
        #
        # Time: O(NM) where N is length of sequence, M is max repeat

        memo = [[0] * 6 for _ in range(n)] # memo[n][x] number of sequences of length n ending at x
        # General cases:
        for i in range(n):
            for x in range(6):
                # Sequence with length i ending at x
                maxRolls = rollMax[x]
                for j in range(i - 1, i - 1 - maxRolls, -1):
                    # Base cases:
                    if j == -1:
                        memo[i][x] += 1
                        break

                    # Sequence with length j ending at non-x
                    for y in range(6):
                        if y != x: memo[i][x] += memo[j][y]

        return sum(memo[-1]) % (10 ** 9 + 7)

