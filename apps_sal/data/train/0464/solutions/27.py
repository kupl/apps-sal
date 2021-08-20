class Solution:

    def minOperations(self, n: int) -> int:
        count = 0
        for i in range(n):
            target = 2 * i + 1
            count += abs(n - target)
        print(count)
        return count // 2
