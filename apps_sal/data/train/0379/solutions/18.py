class Solution:

    def binary_search(self, arr, low, high, x):
        if high >= low:

            mid = (high + low) // 2
            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return -1

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        modulo = 1000000007
        num1Sum = 0
        maxSum = 0
        num2sum = 0
        startIndex = 0
        len2 = len(nums2)
        for num1 in nums1:
            num1InNum2 = self.binary_search(nums2, startIndex, len2 - 1, num1)
            if num1InNum2 != -1:
                num2sum = sum(nums2[startIndex:num1InNum2])
                maxSum += num1Sum if num1Sum > num2sum else num2sum
                maxSum += num1
                num2sum = num1Sum = 0
                startIndex = num1InNum2 + 1
            else:
                num1Sum += num1

        num2sum = sum(nums2[startIndex:])
        maxSum += num1Sum if num1Sum > num2sum else num2sum
        num2sum = num1Sum = 0
        maxSum = maxSum % modulo
        return maxSum
