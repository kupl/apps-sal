class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0] * n
        for i in range(len(arr)):
            arr[i] = (2 * i) + 1
        s = 0
        for i in range(len(arr) // 2):
            s += abs(arr[i] - arr[len(arr) - i - 1])
        return s // 2
