from collections import Counter


class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        if not A:
            return True
        C = Counter(A)
        K = sorted(C.keys())
        for k in K:
            if k == 0:
                if C[k] & 1:
                    return False
                else:
                    C[k] = 0
            if k < 0 and C[k] > 0:
                if k % 2 == 0 and k // 2 in C:
                    C[k // 2] -= C[k]
                    C[k] = 0
            if k > 0 and C[k] > 0:
                if k * 2 in C:
                    C[k * 2] -= C[k]
                    C[k] = 0
        return set(C.values()) == {0}
