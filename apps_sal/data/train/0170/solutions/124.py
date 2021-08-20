from typing import List


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        pre_len = 1
        while pre_len < len(arr):
            if arr[pre_len] < arr[pre_len - 1]:
                break
            pre_len += 1
        arr_a = arr[:pre_len]
        if len(arr_a) == len(arr):
            return 0
        arr_b = [arr[-1]]
        for j in range(len(arr) - 2, -1, -1):
            if arr[j] <= arr[j + 1]:
                arr_b.insert(0, arr[j])
            else:
                break
        ans = len(arr) - 1
        for i in range(len(arr_a)):
            j = self.binary_search(arr_b, arr_a[i])
            cut_length = len(arr) - (i + 1) - (len(arr_b) - j)
            ans = min(ans, cut_length)
        ans = min(ans, len(arr) - len(arr_a))
        ans = min(ans, len(arr) - len(arr_b))
        return ans

    def binary_search(self, arr, num):
        low = 0
        high = len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= num:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans


def __starting_point():
    solution = Solution()
    assert solution.findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) == 3
    assert solution.findLengthOfShortestSubarray([5, 4, 3, 2, 1]) == 4
    assert solution.findLengthOfShortestSubarray([1, 2, 3]) == 0
    assert solution.findLengthOfShortestSubarray([13, 0, 14, 7, 18, 18, 18, 16, 8, 15, 20]) == 8
    assert solution.findLengthOfShortestSubarray([16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15]) == 8


__starting_point()
