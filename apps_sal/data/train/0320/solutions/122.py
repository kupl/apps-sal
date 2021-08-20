class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        max_div = 0
        for n in nums:
            divs = 0
            while n > 0:
                if n % 2:
                    n -= 1
                    ops += 1
                else:
                    n /= 2
                    divs += 1
            max_div = max(max_div, divs)
        return ops + max_div
