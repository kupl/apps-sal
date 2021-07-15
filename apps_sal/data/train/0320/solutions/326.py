class Solution:
    def pow2(self, num):
        addition = 0
        mult = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
                mult += 1
            else:
                num -= 1
                addition += 1
        return (mult, addition)
    
    def minOperations(self, nums: List[int]) -> int:
        result, _ = self.pow2(max(nums))
        for num in nums:
            if num > 0:
                result += self.pow2(num)[1]
        return result
