class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state = 0
        d = {0: - 1}
        vowels = {'a': 1,
                  'e': 2,
                  'i': 4,
                  'o': 8,
                  'u': 16}
        max_len = 0
        for i in range(len(s)):
            if s[i] in vowels:
                state ^= vowels[s[i]]
                if state not in d:
                    d[state] = i

            if state in d:
                max_len = max(max_len, i - d[state])

        return max_len
