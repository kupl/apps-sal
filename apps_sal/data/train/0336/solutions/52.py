class Solution:
    from collections import defaultdict

    def minSteps(self, s: str, t: str) -> int:
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1
        for c in t:
            counts[c] -= 1

        return sum(abs(counts[d]) for d in counts) // 2
