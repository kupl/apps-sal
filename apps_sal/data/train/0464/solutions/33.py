class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        min_operations = 0
        for i in range(n):
            arr.append((2 * i) + 1)
        target = sum(arr) // n
        middle = ceil(n / 2)
        # print(arr, target, middle)
        for i in range(ceil(n / 2)):
            min_operations += (target - arr[i])
        return min_operations

# 1 - 0
# 2 - 1
# 3 - 2
# 4 - 4
# 5 - 6
# 6 - 9
