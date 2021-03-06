from collections import defaultdict


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrFreq = defaultdict(int)
        charFreq = defaultdict(int)
        curr_substr = []
        l = 0
        r = l + minSize - 1
        while l < len(s):
            for ch in s[l:r]:
                curr_substr.append(ch)
                charFreq[ch] += 1
            while r - l + 1 <= maxSize and r < len(s):
                charFreq[s[r]] += 1
                curr_substr.append(s[r])
                if len(charFreq) <= maxLetters:
                    substrFreq[''.join(curr_substr)] += 1
                r += 1
            curr_substr = []
            charFreq = defaultdict(int)
            l += 1
            r = l + minSize - 1
        if substrFreq:
            return max(substrFreq.values())
        return 0
