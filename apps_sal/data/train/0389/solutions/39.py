class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        N = len(A)

        if N <= 1:
            return False

        max_sum = sum(A)
        sums = [0] * (max_sum + 1)
        for i in range(N):
            num = A[i]
            for s in range(max_sum, num - 1, -1):
                if sums[s - num]:
                    sums[s] |= sums[s - num] << 1
            sums[num] |= 1
        for l in range(1, N):
            s = (max_sum * l) / N
            if s.is_integer() and (sums[int(s)] >> (l - 1)) & 1:
                return True
        return False
