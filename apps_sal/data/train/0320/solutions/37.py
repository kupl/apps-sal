class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        maxi = 0
        for num in nums:
            res += 1 if num > 0 else 0
            div = 0
            while num > 1:
                res += 1 if num % 2 else 0
                num //= 2
                div += 1
            maxi = max(div, maxi)
        return res + maxi
