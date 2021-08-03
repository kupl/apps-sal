class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        def valid(sub):
            seen = set()
            for c in sub:
                seen.add(c)
            return len(seen)

        counts = dict()
        start = 0
        while start < len(s):
            end = start + minSize
            while end <= len(s) and end <= start + maxSize:
                sub = s[start:end]
                if sub in counts:
                    counts[sub] += 1
                else:
                    num_letters = valid(sub)
                    if num_letters <= maxLetters:
                        counts[sub] = 1
                    else:
                        break
                end += 1
            start += 1

        l = list(counts.values())
        if len(l) == 0:
            return 0
        return max(l)
