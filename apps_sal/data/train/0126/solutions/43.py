class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrings = defaultdict(int)
        for gap in range(minSize, maxSize + 1):
            for start in range(len(s) - gap + 1):
                end = start + gap
                substrings[s[start:end]] += 1
        max_ = 0
        for (substring, times) in substrings.items():
            if times > max_ and len(set(substring)) <= maxLetters:
                max_ = times
        return max_
