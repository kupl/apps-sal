class Solution:
    def minOperations(self, nums: List[int]) -> int:
        arr = nums[:]
        res = 0
        while any(arr):
            odd = sum([x % 2 == 1 for x in arr])
            if odd:
                arr = [x - x % 2 for x in arr]
                res += odd
            else:
                arr = [x // 2 for x in arr]
                res += 1
        return res

