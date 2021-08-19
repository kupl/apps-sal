class Solution:

    def maximumSwap(self, num):
        arr = str(num)
        n = len(arr)
        posmax = [0] * n
        posmax[-1] = n - 1
        pow10 = [0] * n
        pow10[-1] = 1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[posmax[i + 1]]:
                posmax[i] = i
            else:
                posmax[i] = posmax[i + 1]
            pow10[i] = pow10[i + 1] * 10
        for i in range(n):
            if arr[i] == '9':
                continue
            j = posmax[i]
            if arr[j] > arr[i]:
                x = int(arr[i])
                y = int(arr[j])
                return num + pow10[i] * (-x + y) + pow10[j] * (-y + x)
        return num
