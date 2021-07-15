class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        comparisons = [a >= b for a,b in zip(sorted(s1), sorted(s2))]
        all_true = all(comparisons)
        if not all_true:
            comparisons = [a <= b for a,b in zip(sorted(s1), sorted(s2))]
            all_true = all(comparisons)
        return all_true
