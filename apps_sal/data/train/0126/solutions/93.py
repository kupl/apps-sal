class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        all_substrings = {}
        max_letters = maxLetters
        min_size = minSize
        max_size = maxSize
        _s = s
        max = 0
        for i in range(min_size, max_size + 1):
            for j in range(len(_s) - i + 1):
                ss = _s[j:j + i]
                if len(set(ss)) <= max_letters:
                    if ss not in all_substrings:
                        all_substrings[ss] = 0
                    all_substrings[ss] += 1
                    if all_substrings[ss] > max:
                        max = all_substrings[ss]
        return max
