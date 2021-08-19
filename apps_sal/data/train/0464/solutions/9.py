class Solution:

    def minOperations(self, n: int) -> int:
        count = sum([x * 2 for x in range((n + 1) // 2)])
        if n % 2 == 0:
            count += n // 2
        return count
