class Solution:

    def minOperations(self, n: int) -> int:
        arr = [i * 2 + 1 for i in range(n)]
        if n % 2 == 0:
            median = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2
            return sum((arr[i] - median for i in range(n // 2 + 1, n))) + 1
        else:
            median = arr[len(arr) // 2]
            return sum((arr[i] - median for i in range(n // 2 + 1, n)))
