class Solution:
    def minOperations(self, n: int) -> int:
        avg = n

        count = 0
        for i in range((n // 2)):
            count += avg - (2 * i + 1)

        return count
