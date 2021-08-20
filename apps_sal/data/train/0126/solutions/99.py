class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        dict = {}
        for i in range(len(s)):
            for j in range(i + minSize, i + maxSize + 1):
                if j <= len(s):
                    substr = s[i:j]
                    if len(set(substr)) <= maxLetters:
                        if substr in dict:
                            dict[substr] += 1
                        else:
                            dict[substr] = 1
        max_count = 0
        for (k, v) in list(dict.items()):
            max_count = max(max_count, v)
        return max_count
