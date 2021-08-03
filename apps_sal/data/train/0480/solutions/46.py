MOD = int(1e9 + 7)


class Solution:
    def get_count(self, counts, i):
        if i < 0 or i >= len(counts):
            return 0
        else:
            return counts[i]

    def numWays(self, steps: int, arrLen: int) -> int:
        counts = [1]
        for si in range(1, steps + 1):
            new_len = min(si + 1, arrLen)
            new_counts = [0] * new_len
            for i in range(new_len):
                new_counts[i] = sum(self.get_count(counts, j) for j in range(i - 1, i + 1 + 1)) % MOD
            counts = new_counts
        return counts[0]
