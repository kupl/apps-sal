class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()

        n = len(A)

        total = 0

        for i, a in enumerate(A):
            left = i  # how many elements on the left
            right = n - i - 1  # how many elements on the right
            # number of subsequences with A[i] as max is (2 ** left)
            total += (2 ** left - 1) * a  # minus 1 so subsequence with only A[i] is not counted
            total -= (2 ** right - 1) * a

        return total % (10 ** 9 + 7)
