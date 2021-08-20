class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0
        bar = k * threshold
        total = 0
        window = sum(arr[:k])
        if window >= bar:
            total += 1
        for i in range(k, len(arr)):
            window -= arr[i - k]
            window += arr[i]
            if window >= bar:
                total += 1
        return total
