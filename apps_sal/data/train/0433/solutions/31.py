class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        min_sum = k * threshold
        running_sum = sum(arr[0:k])
        if running_sum >= min_sum:
            count = 1
        else:
            count = 0
        for i in range(len(arr) - k):
            running_sum -= arr[i]
            running_sum += arr[i + k]
            if running_sum >= min_sum:
                count += 1
        return count
