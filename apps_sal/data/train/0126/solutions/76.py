class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = dict()
        for i in range(minSize, maxSize + 1):
            for j in range(i, len(s) + 1):
                curr = s[j - i:j]
                if curr not in counts:
                    if len(set(curr)) <= maxLetters:
                        counts[curr] = 1
                else:
                    counts[curr] += 1
        if not counts:
            return 0
        else:
            return max(counts.values())
