class Solution:

    def wiggleMaxLength(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)
        if n < 2:
            return n
        wsl = [0] * n
        wsl[0] = 1
        for cur in range(1, n):
            prev = cur - 1
            if arr[cur] > arr[prev] and wsl[prev] <= 1:
                wsl[cur] = abs(wsl[prev]) + 1
            elif arr[cur] < arr[prev] and wsl[prev] > 0:
                wsl[cur] = (abs(wsl[prev]) + 1) * -1
            else:
                wsl[cur] = wsl[prev]
        return abs(wsl[n - 1])
