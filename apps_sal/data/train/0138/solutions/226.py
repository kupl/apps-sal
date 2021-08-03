class Solution:
    # Any subarray containing a zero must be broken into seperate subarrays either side of the zero
    # Any subarr with an even number of negatives can be counted in its entirety
    # For a subarr with an odd number of negatives, the largest subarray excluding either the left or rightmost negative number can be taken instead

    def getMaxLen(self, nums: List[int]) -> int:
        # Simplify array to +-1
        for i in nums:
            if i > 0:
                i = 1
            elif i < 0:
                i = -1

        arrays = []
        end = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                arrays.append(nums[end:i])
                end = i + 1
        arrays.append(nums[end:])

        # print(arrays)
        maximum = 0
        for arr in arrays:
            maxi = 0
            neg = 0
            first = -1
            for i in range(len(arr)):
                if arr[i] < 0:
                    neg += 1
                    if first == -1:
                        first = i + 1
                    last = i
            if neg % 2 == 0:
                maxi = len(arr)
            else:
                # Length of sub a (missing first)
                subA = len(arr) - first
                # Length of sub b (missing last)
                subB = last
                maxi = max(subA, subB)
            #print(arr, maxi)
            maximum = max(maximum, maxi)

        return maximum
