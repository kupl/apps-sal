class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        found = collections.defaultdict(int)
        for sl in range(minSize, min(len(s), maxSize) + 1):
            for start_index in range(len(s) - sl + 1):
                substring = s[start_index:start_index + sl]
                if len(set(substring)) <= maxLetters:
                    found[substring] += 1

        vals = sorted(found.values())
        if len(vals) == 0:
            return 0
        return vals[-1]
