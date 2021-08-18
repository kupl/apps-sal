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

        try:
            i, x, y = next((i, x, y) for i, (x, y) in enumerate(zip(A, suff_max)) if x != y)
        except StopIteration:
            return num

        A[i], A[last[y]] = A[last[y]], A[i]

        return int(''.join(A))
