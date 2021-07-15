class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans, largest = 0, 0
        for num in nums:
            largest = max(largest, num)
            while num > 0:
                if num % 2 == 1:
                    num -= 1
                    ans += 1
                if num > 0:
                    num = num // 2
        while largest > 1:
            ans += 1
            largest = largest // 2
        return ans
