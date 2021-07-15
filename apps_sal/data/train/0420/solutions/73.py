class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        substrings = self.generate_subst(s)
        res = 0
        for substring in substrings:
            is_all_even = True
            for ch in 'aeiou':
                if substring.count(ch) % 2:
                    is_all_even = False
                    break
            if is_all_even:
                return len(substring)
        return res

    def generate_subst(self, s: str):
        for window_size in range(len(s), -1, -1):
            for i in range(len(s) - window_size + 1):
                yield s[i: i+window_size]
