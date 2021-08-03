class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()

        n = len(A)

        total = 0

        for i in range(n):
            a = A[i]

            left = i  # how many elements on the left
            right = n - i - 1  # how many elements on the right
            # number of subsequences with A[i] as max is (2 ** left)
            total += ((1 << left) - 1) * a  # minus 1 so subsequence with only A[i] is not counted
            total -= ((1 << right) - 1) * a

        return total % (10 ** 9 + 7)
