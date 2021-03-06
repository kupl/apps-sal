class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans = 0
        str_freq = collections.Counter()
        for i in range(len(s) - minSize + 1):
            candidate = s[i:i + minSize]
            if len(set(candidate)) <= maxLetters:
                str_freq[candidate] += 1
                ans = max(ans, str_freq[candidate])
        return ans
