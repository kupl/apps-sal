class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        subs = {}
        i = j = 0
        chars = {}
        while i < len(s):
            if j < len(s) and (s[j] in chars or len(chars) < maxLetters):
                if s[j] not in chars:
                    chars[s[j]] = 0
                chars[s[j]] += 1
                j += 1
            else:
                for k in range(i + minSize, min(i + maxSize, j) + 1):
                    sub = s[i:k]
                    if sub not in subs:
                        subs[sub] = 0
                    subs[sub] += 1
                chars[s[i]] -= 1
                if chars[s[i]] == 0:
                    del chars[s[i]]
                i += 1
        return max(list(subs.values()) or [0])
