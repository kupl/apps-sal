class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        seen = collections.defaultdict(int)
        n = len(s)
        for k in range(minSize, maxSize + 1):
            counts = collections.Counter(s[:k])
            if len(counts) <= maxLetters:
                seen[s[:k]] += 1
            for i in range(n - k):
                counts[s[i]] -= 1
                if counts[s[i]] == 0:
                    del counts[s[i]]
                counts[s[i + k]] += 1
                if len(counts) <= maxLetters:
                    seen[s[i + 1:i + k + 1]] += 1
        return max(seen.values()) if len(seen) > 0 else 0
