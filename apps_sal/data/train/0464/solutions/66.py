class Solution:

    def minOperations(self, n: int) -> int:
        arr = [0] * n
        for i in range(n):
            arr[i] = 2 * i + 1
        print(arr)
        k = arr[int(len(arr) / 2)]
        print(k)
        total = 0
        for i in range(len(arr)):
            p = int(arr[i])
            total = total + abs(k - p)
        return int(total / 2)
