class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A = sorted(A, key=lambda x: abs(x))
        M = Counter()

        for e in A:
            M[e] += 1

        # print(M)
        # print(A)

        for e in A:
            # print(e, M[2*e], M)
            if M[e] and M[2 * e]:
                M[2 * e] -= 1
                M[e] -= 1
                # print('->', 2*e, M[2*e])
            elif M[e]:
                # print(M, e)
                return False
        return True
