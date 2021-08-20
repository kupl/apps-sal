class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        arr = list(accumulate(arr))
        count = 0
        (prev_even, prev_odd) = (0, 0)
        for i in range(len(arr)):
            if arr[i] % 2:
                count += 1
                count += prev_even
                prev_odd += 1
            else:
                count += prev_odd
                prev_even += 1
        return count % (10 ** 9 + 7)
