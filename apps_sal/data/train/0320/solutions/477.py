class Solution:
    def minOperations(self, nums: List[int]) -> int:
        _max = -1
        ans = 0
        for x in nums:
            ans += bin(x).count('1')
            _max = max(_max, x)

        ans += len(bin(_max)) - 3

        return ans
