class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        counter = 0
        for i in range(len(arr)):
            if i - k >= 0:
                if (arr[i] - arr[i - k]) / k >= threshold:
                    counter += 1
            elif i - k == -1:
                if arr[i] / k >= threshold:
                    counter += 1
        return counter
