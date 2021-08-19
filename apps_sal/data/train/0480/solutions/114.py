class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        counts = [0] * min(arrLen, steps + 1)
        (counts[0], counts[1]) = (1, 1)
        mod = 10 ** 9 + 7
        while steps - 1:
            prev_counts = counts[:]
            for i in range(len(counts)):
                if i == 0:
                    counts[i] = sum(prev_counts[i:i + 2]) % mod
                elif i == arrLen - 1:
                    counts[i] = sum(prev_counts[i - 1:i + 1]) % mod
                else:
                    counts[i] = sum(prev_counts[i - 1:i + 2]) % mod
            steps -= 1
        return counts[0]
