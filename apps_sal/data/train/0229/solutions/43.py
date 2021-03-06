from collections import Counter


class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        if not A:
            return True
        counts = Counter(A)
        for key in sorted(counts.keys()):
            if counts[key] == 0:
                continue
            factor = 0.5 if key < 0 else 2
            if counts[key] > counts[factor * key]:
                return False
            counts[factor * key] -= counts[key]
        return True
