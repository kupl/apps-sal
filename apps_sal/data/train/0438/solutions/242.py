class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        border = [0] * (len(arr) + 2)
        ans = -1
        for i in range(len(arr)):
            left = right = arr[i]
            if border[right + 1] > 0:
                right = border[right + 1]
            if border[left - 1] > 0:
                left = border[left - 1]
            (border[left], border[right]) = (right, left)
            if right - arr[i] == m or arr[i] - left == m:
                ans = i
        return ans
