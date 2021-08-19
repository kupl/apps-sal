class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        border = [0] * (n + 2)
        ans = -1
        for i in range(n):
            left = right = arr[i]
            if border[right + 1] > 0:
                right = border[right + 1]
            if border[left - 1] > 0:
                left = border[left - 1]
            (border[left], border[right]) = (right, left)
            if right - arr[i] == m or arr[i] - left == m:
                ans = i
        return ans
