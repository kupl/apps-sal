from collections import Counter
from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = Counter(s[:minSize - 1])
        substrs = defaultdict(int)
        start = 0
        for end in range(minSize - 1, len(s)):
            counts[s[end]] += 1
            if end - start + 1 > minSize:
                counts[s[start]] -= 1
                start += 1
            if end - start + 1 == minSize and len(set(counts.elements())) <= maxLetters:
                substrs[s[start:end + 1]] += 1
        if not substrs:
            return 0
        return max(substrs.values())
