class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = Counter()
        for k in range(minSize, maxSize + 1):
            window = Counter(s[:k])
            if len(window) <= maxLetters:
                count[s[:k]] += 1
            for i in range(k, len(s)):
                window[s[i]] += 1
                window[s[i - k]] -= 1
                if window[s[i - k]] == 0:
                    del window[s[i - k]]
                if len(window) <= maxLetters:
                    count[s[i - k + 1:i + 1]] += 1
        return max(list(count.values()), default=0)

