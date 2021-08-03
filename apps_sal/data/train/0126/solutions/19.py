class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = 0
        n = len(s)
        count = Counter()

        for i in range(n - minSize + 1):

            r = i + minSize
            seen = {c for c in s[i:r]}
            unique = len(seen)
            while unique <= maxLetters and r <= n and r - i <= maxSize:
                if s[r - 1] not in seen:
                    unique += 1
                    seen.add(s[r - 1])
                count[s[i:r]] += 1
                r += 1

        return max(count.values()) if count else 0
