class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        arr = [-1e99] + arr + [1e99]

        left_p = 0
        while left_p + 1 < len(arr) and arr[left_p] <= arr[left_p + 1]:
            left_p += 1

        right_p = len(arr) - 1
        while right_p - 1 >= 0 and arr[right_p] >= arr[right_p - 1]:
            right_p -= 1
        right_p_old = right_p
        if left_p > right_p:
            return 0

        while arr[right_p] < arr[left_p]:
            right_p += 1
        to_ret = right_p - left_p - 1

        while right_p >= right_p_old and left_p > 0:
            left_p -= 1
            while right_p - 1 >= right_p_old and arr[right_p - 1] >= arr[left_p]:
                right_p -= 1
            to_ret = min(to_ret, right_p - left_p - 1)

        return to_ret

        # 10 2 99 12 13
