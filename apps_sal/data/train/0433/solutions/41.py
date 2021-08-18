class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sumThreshold = k * threshold
        arrLength = len(arr)
        currentSum = 0
        for i in range(k):
            currentSum += arr[i]
        count = 0
        if currentSum >= sumThreshold:
            count += 1
        for i in range(k, arrLength):
            currentSum += arr[i] - arr[i - k]
            if currentSum >= sumThreshold:
                count += 1
        return count
