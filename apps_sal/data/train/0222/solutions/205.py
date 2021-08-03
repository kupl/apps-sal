import collections


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dict1 = collections.defaultdict(lambda: 2)
        L = len(A)
        set_A = set(A)
        if L < 3:
            return 0
        d = 2
        for i, A_i in enumerate(A):
            for j in range(i, 0, -1):
                if A_i - A[j] > A[j]:
                    break
                elif A_i - A[j] in set_A:
                    dd = dict1[A_i - A[j], A[j]] + 1
                    dict1[A[j], A_i] = dd
                    d = max(d, dd)
        return d if d > 2 else 0
