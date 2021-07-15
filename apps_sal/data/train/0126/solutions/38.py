class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        all_substrings = {}
        max_letters = maxLetters
        min_size = minSize
        max_size = maxSize
        _s = s
        ll = len(_s)
        for i in range(min_size, max_size + 1):
            for j in range(ll - i + 1):
                ss = _s[j:j+i]
                if max_letters >= min_size or len(set(ss)) <= max_letters:
                    if ss not in all_substrings:
                        all_substrings[ss] = 1
                    else:
                        all_substrings[ss] += 1
        return max(all_substrings.values()) if len(all_substrings) > 0 else 0
