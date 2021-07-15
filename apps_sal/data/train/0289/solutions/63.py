class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        Len = len(A) + 1
        prefix = [0] + A
        maxSum = 0
        for i in range(1, Len):
            prefix[i] = prefix[i - 1] + A[i - 1]
        i = L
        while i < Len:
            LSum = prefix[i] - prefix[i - L]
            j = M
            while j < i - L:
                MSum = prefix[j] - prefix[j - M]
                temp = LSum + MSum
                if temp > maxSum:
                    maxSum = LSum + MSum
                j += 1
            j = i + M
            while j < Len:
                MSum = prefix[j] - prefix[j - M]
                temp = LSum + MSum
                if temp > maxSum:
                    maxSum = temp
                j += 1
            i += 1
        return maxSum
