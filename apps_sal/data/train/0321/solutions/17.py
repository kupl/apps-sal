class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        indices = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]
        comparisons = [s1[i] > s2[i] for i in indices]
        return all(comparisons) or (not any(comparisons))
