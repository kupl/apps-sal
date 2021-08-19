class Solution:

    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        arr = [int(ch) for ch in str(N)]
        marker = len(arr)
        i = len(arr) - 2
        while i >= 0:
            if arr[i] > arr[i + 1]:
                marker = i + 1
                arr[i] -= 1
            i -= 1
        while marker < len(arr):
            arr[marker] = 9
            marker += 1
        return int(''.join([str(num) for num in arr]))
