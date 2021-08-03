class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:

        res = 0

        # the order does not matter with subsequeces so first sort the array
        A.sort()

        for i in range(len(A)):
            # then at position i, we know that there are i smaller numbers and 2^i different subsequences where i will be the maximum, so we add 2^i times A[i]
            res += (2**i) * A[i]
            # Also, A[i] will be less than len(A) - i - 1 numbers or (2^len(A)-1-i) different combinations, so subtract that
            res -= (2**(len(A) - 1 - i)) * A[i]

        return res % ((10**9) + 7)
