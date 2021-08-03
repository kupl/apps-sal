class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append((2 * i) + 1)
        s = sum(arr) // n
        res = 0
        for i in range(n // 2):
            res += s - arr[i]
        return res
