class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        rolling_sum = sum(arr[:k])
        count = 0 if rolling_sum < threshold * k else 1
        for i in range(len(arr) - k):
            rolling_sum = rolling_sum - arr[i] + arr[i + k]
            if rolling_sum >= threshold * k:
                count += 1
        return count
