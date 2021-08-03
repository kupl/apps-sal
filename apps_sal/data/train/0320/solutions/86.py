import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        arr = nums.copy()
        count = result = 0

        while any(arr):

            for i, n in enumerate(arr):
                if n & 1:
                    count += 1
                    arr[i] -= 1

            result += count
            arr = [x >> 1 for x in arr]
            count = 0

        return result + int(math.log2(max(nums)))
