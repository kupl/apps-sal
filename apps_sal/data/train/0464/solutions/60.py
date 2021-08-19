class Solution:

    def minOperations(self, n: int) -> int:
        res = 0
        arr = [2 * i + 1 for i in range(n)]
        for item in arr:
            if item < n:
                res += n - item
            else:
                break
        return res
