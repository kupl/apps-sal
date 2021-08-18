class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        seen = collections.defaultdict(int)
        n = len(s)
        counts = collections.Counter(s[:minSize])
        if len(counts) <= maxLetters:
            seen[s[:minSize]] += 1
        for i in range(n - minSize):
            counts[s[i]] -= 1
            if counts[s[i]] == 0:
                del counts[s[i]]
            counts[s[i + minSize]] += 1
            if len(counts) <= maxLetters:
                seen[s[i + 1:i + minSize + 1]] += 1
        return max(seen.values()) if len(seen) > 0 else 0
