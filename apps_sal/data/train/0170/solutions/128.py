class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left_idx, right_idx = 0, n - 1
        while left_idx < n - 1 and arr[left_idx] <= arr[left_idx + 1]:
            left_idx += 1
        while right_idx > 0 and arr[right_idx - 1] <= arr[right_idx]:
            right_idx -= 1
        nums_to_rm = min(n - left_idx - 1, right_idx)

        for curr_idx in range(left_idx + 1):
            if arr[curr_idx] <= arr[right_idx]:
                nums_to_rm = min(nums_to_rm, max(0, right_idx - curr_idx - 1))
            else:
                if right_idx < n - 1:
                    right_idx += 1
                else:
                    break
        return nums_to_rm
