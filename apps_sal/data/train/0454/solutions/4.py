class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        import itertools

        A = [c for c in str(num)]

        suff_max = list(itertools.accumulate(A[::-1], max))[::-1]

        last = {x: i for i, x in enumerate(A)}

        for i, x in enumerate(A):
            if x < suff_max[i]:
                A[i], A[last[suff_max[i]]] = A[last[suff_max[i]]], A[i]
                break

        return int(''.join(A))
