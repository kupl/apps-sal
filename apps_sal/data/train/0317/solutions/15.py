class Solution:

    def numPermsDISequence(self, S: str) -> int:
        d = [0] * (len(S) + 1)
        d[0] = 1
        for (i, c) in enumerate(S):
            if c == 'D':
                for j in range(i - 1, -1, -1):
                    d[j] += d[j + 1]
            else:
                for j in range(1, i + 1):
                    d[j] += d[j - 1]
                for j in range(i + 1, 0, -1):
                    d[j] = d[j - 1]
                d[0] = 0
        return sum(d) % 1000000007
