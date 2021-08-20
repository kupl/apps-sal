class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        S = sum(A)
        L = len(A)
        if L == 1:
            return False
        sizes = {(0, 0)}
        for n in A:
            for (s, c) in sizes.copy():
                if c < L // 2:
                    sizes.add((s + n, c + 1))
        sizes.remove((0, 0))
        for (s, c) in sizes:
            if s * (L - c) == (S - s) * c:
                return True
        return False
