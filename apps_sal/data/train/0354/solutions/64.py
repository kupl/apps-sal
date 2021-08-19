class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # Idea:
        #   DP with optimal substructure where:
        #       number of sequences of length N ending at X is sum of:
        #           number of sequences of length N - 1 ending at non-X (also seq of len N ending with X)
        #           number of sequences of length N - 2 ending at non-X (also seq of len N ending with XX)
        #           ...
        #           number of sequences of length N - C ending at non-X (also seq of len N ending with XX...X)
        #
        #       where C is number of max repeats
        #
        # Time: O(NM) where N is length of sequence, M is max repeat

        memo = [[0] * 6 for _ in range(n)]  # memo[n][x] number of sequences of length n ending at x
        # General cases:
        for i in range(n):
            for x in range(6):
                # Sequence with length i ending at x
                maxRepeats = rollMax[x]
                for j in range(i - 1, i - 1 - maxRepeats, -1):
                    # Base cases:
                    if j == -1:
                        memo[i][x] += 1
                        break

                    # Sequence with length j ending at non-x
                    for y in range(6):
                        if y != x:
                            memo[i][x] += memo[j][y]

        return sum(memo[-1]) % (10 ** 9 + 7)
