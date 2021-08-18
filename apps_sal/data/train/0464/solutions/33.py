class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        min_operations = 0
        for i in range(n):
            arr.append((2 * i) + 1)
        target = sum(arr) // n
        middle = ceil(n / 2)
        for i in range(ceil(n / 2)):
            min_operations += (target - arr[i])
        return min_operations
