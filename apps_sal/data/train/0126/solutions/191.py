from collections import Counter
from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)
        substrs = defaultdict(int)
        start = 0
        for end in range(len(s)):
            counts[s[end]] += 1
            if end - start + 1 > minSize:
                counts[s[start]] -= 1
                if counts[s[start]] == 0:
                    del counts[s[start]]
                start += 1
            print(counts)
            if end - start + 1 == minSize and len(counts) <= maxLetters:
                substrs[s[start:end + 1]] += 1
        print(substrs)
        if not substrs:
            return 0
        return max(substrs.values())
