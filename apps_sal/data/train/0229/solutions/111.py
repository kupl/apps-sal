class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        A = sorted(A, key=lambda x: abs(x))
        M = Counter()
        for e in A:
            M[e] += 1
        for e in A:
            if M[e] and M[2 * e]:
                M[2 * e] -= 1
                M[e] -= 1
            elif M[e]:
                return False
        return True
