from itertools import accumulate


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # How many non-empty subarrays are there from an array of length k
        def num_subarrays(k):
            return (k * k + k) // 2
        counts = [0, 0]
        for prefix in accumulate(arr):
            counts[prefix % 2] += 1
        evens, odds = counts
        return (num_subarrays(len(arr)) - (num_subarrays(evens) + (num_subarrays(odds) - odds))) % (10 ** 9 + 7)
