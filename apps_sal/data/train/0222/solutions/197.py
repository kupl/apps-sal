from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        d = defaultdict(lambda: 1)
        set_A = set(A)

        for first in range(len(A)):
            for second in range(first + 1, len(A)):
                if A[second] - A[first] in set_A and A[first] > A[second] - A[first]:
                    d[A[first], A[second]] = d[A[second] - A[first], A[first]] + 1

        if len(d.values()) == 0:
            return 0
        ret = max(d.values()) + 1
        return ret if ret >= 3 else 0
