class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        evenCount, oddCount = 1, 0
        totalSum = numArrays = 0

        for val in arr:
            totalSum += val
            numArrays += evenCount if totalSum % 2 else oddCount
            evenCount += totalSum % 2 == 0
            oddCount += totalSum % 2 == 1

        return numArrays % ((10**9) + 7)
