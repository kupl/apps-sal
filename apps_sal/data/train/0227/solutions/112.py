class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = []
        count = 0
        maxCount = 0
        for i in range(len(A)):
            if A[i] == 0:
                zeroes.insert(0, i)

            if len(zeroes) > K:
                count = i - zeroes.pop()
            else:
                count += 1
            maxCount = max(maxCount, count)
        return maxCount
