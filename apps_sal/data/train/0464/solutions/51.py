class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            target = n + 1
            count = 0
            i = 1
            while i <= n:
                count += abs(target - 2 * i + 1)
                i += 1
            return count // 2
