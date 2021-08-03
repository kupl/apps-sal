class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0

        subarray = 0
        for i in range(k):
            subarray += arr[i]
        average = subarray / k

        if average >= threshold:
            total += 1

        for i in range(len(arr) - k):
            subarray = subarray - arr[i] + arr[i + k]
            average = subarray / k
            if average >= threshold:
                total += 1

        return total
