class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.defaultdict(int)
        for k in range(minSize, minSize + 1):
            counter = collections.Counter(s[:k])
            for i in range(k, len(s)):
                if len(counter.keys()) <= maxLetters:
                    res[s[i - k:i]] += 1
                counter[s[i]] += 1
                counter[s[i - k]] -= 1
                if counter[s[i - k]] == 0:
                    del counter[s[i - k]]
            if len(counter.keys()) <= maxLetters:
                res[s[i - k + 1:]] += 1
        return max(res.values()) if res else 0
