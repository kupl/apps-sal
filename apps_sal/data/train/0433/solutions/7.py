class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0

        prevAverage = 0
        counter = 0
        for i in range(len(arr) - k + 1):
            if i == 0:
                average = sum(arr[i:i + k]) / k
            else:
                average = (prevAverage * k - (arr[i - 1]) + arr[i + k - 1]) / k

            if average >= threshold:
                counter += 1

            #print(arr[i:i+k], prevAverage, average)

            prevAverage = average

        return counter
