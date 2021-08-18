class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        N = len(A)

        if N <= 1:
            return False

        max_sum = sum(A)
        print(max_sum)
        sums = [0] * (max_sum + 1)
        for i in range(N):
            num = A[i]
            for s in range(max_sum, num - 1, -1):
                if sums[s - num]:
                    sums[s] |= sums[s - num] << 1
            sums[num] |= 1
        for s in range(max_sum + 1):
            for i in range(N - 1):
                if (sums[s] >> i) & 1:
                    mean = s / (i + 1)
                    rem = (max_sum - s) / (N - (i + 1))
                    if mean == rem:
                        return True

        return False
