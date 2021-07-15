class Solution:
    def __init__(self):
        self.counter = 0
        self.threshold = 0
        self.k = 0

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        self.k = k
        self.threshold = threshold

        interval = sum(arr[:k])
        self._count_if_slice_sum_passes_threshold(interval)

        left = 0
        while left + k < len(arr):
            interval -= arr[left]
            left += 1
            right = left + k - 1
            interval += arr[right]
            self._count_if_slice_sum_passes_threshold(interval)
        return self.counter

    def _count_if_slice_sum_passes_threshold(self, slice):
        if slice / self.k >= self.threshold:
            self.counter += 1
