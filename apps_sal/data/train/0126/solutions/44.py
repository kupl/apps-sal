class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if maxLetters == 0:
            return 0
        sw = collections.defaultdict(int)
        substrings = collections.defaultdict(int)
        l = 0
        res = 0
        for (r, ch) in enumerate(s):
            sw[ch] += 1
            while l <= r and len(sw) > maxLetters:
                chL = s[l]
                sw[chL] -= 1
                if sw[chL] == 0:
                    del sw[chL]
                l += 1
            for j in range(r + 1 - maxSize, r + 1 - minSize + 1):
                if j < l:
                    continue
                substrings[s[j:r + 1]] += 1
                res = max(res, substrings[s[j:r + 1]])
        return res
