class Solution:
    def numSplits(self, s: str) -> int:
        left = [0] * len(s)

        unique = set()
        n_distinct = 0
        for i, l in enumerate(s):
            if l not in unique:
                unique.add(l)
                n_distinct += 1
            left[i] = n_distinct

        count = 0
        unique = set()
        n_distinct = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] not in unique:
                unique.add(s[i])
                n_distinct += 1

            if n_distinct == left[i - 1]:
                count += 1

        return count
