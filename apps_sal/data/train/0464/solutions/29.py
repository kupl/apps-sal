class Solution:

    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        target = sum(arr) // n
        res = 0
        for i in range(n // 2):
            res += abs(target - arr[i])
        return res
