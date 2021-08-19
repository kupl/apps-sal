class Solution:

    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        avg = int(sum(arr) / len(arr))
        return sum([abs(a - avg) for a in arr]) // 2
