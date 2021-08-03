class Solution:
    def maxFreq(self, S, maxchars, minsize, maxsize):
        n = len(S)
        freq = Counter()
        chars = Counter()
        i = 0
        for j in range(n):
            if j - i + 1 > minsize:
                chars[S[i]] -= 1
                if chars[S[i]] == 0:
                    del chars[S[i]]
                i += 1
            chars[S[j]] += 1
            if j - i + 1 >= minsize:
                if len(chars) <= maxchars:
                    freq[S[i:j + 1]] += 1
        return max(freq.values(), default=0)
