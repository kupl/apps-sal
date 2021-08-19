class Solution:

    def uniqueLetterString(self, s: str) -> int:
        index = {char: [-1] + [ic for (ic, char0) in enumerate(s) if char == char0] + [len(s)] for char in set(s)}
        return sum([(index[char][jj] - index[char][jj - 1]) * (index[char][jj + 1] - index[char][jj]) for char in index for jj in range(1, len(index[char]) - 1)])
