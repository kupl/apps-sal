class Solution:

    def minOperations(self, nums: List[int]) -> int:
        maxDoubles = 0
        incrs = 0
        for num in nums:
            doubles = 0
            while num > 0:
                if num % 2 == 1:
                    incrs += 1
                    num -= 1
                else:
                    doubles += 1
                    num >>= 1
            maxDoubles = max(maxDoubles, doubles)
        return incrs + maxDoubles
