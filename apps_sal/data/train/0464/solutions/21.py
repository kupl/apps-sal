class Solution:

    def minOperations(self, n: int) -> int:
        arr = [i for i in range(1, n * 2, 2)]
        target = 0
        ops = 0
        if n % 2 == 1:
            idx = n // 2
            target = arr[idx]
        else:
            right = n // 2
            left = right - 1
            print(right)
            print(left)
            print(arr)
            target = arr[left] + 1
        for j in range(n // 2):
            diff = target - arr[j]
            ops += diff
        return ops
