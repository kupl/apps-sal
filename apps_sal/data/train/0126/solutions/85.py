class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        all_substrings = {}
        for i in range(minSize, maxSize + 1):
            for j in range(len(s) - i + 1):
                ss = s[j:j + i]
                if len(set(ss)) <= maxLetters:
                    if ss not in all_substrings:
                        all_substrings[ss] = 0
                    all_substrings[ss] += 1
        if len(all_substrings) > 0:
            return max(all_substrings.values())
        else:
            return 0
