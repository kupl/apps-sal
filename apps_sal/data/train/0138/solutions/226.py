class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
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
                subA = len(arr) - first
                subB = last
                maxi = max(subA, subB)
            maximum = max(maximum, maxi)

        return maximum
