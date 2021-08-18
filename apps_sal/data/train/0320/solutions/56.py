from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_doubles = 0
        increments = 0

        counts = Counter(nums)
        for n, c in counts.items():
            if n == 0:
                continue
            doubles = 0
            while n:
                if n % 2 == 1:
                    increments += c
                    n -= 1
                else:
                    doubles += 1
                    n //= 2
            max_doubles = max(max_doubles, doubles)

        return increments + max_doubles
