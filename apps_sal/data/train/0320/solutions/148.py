class Solution:

    def minOperations(self, nums: List[int]) -> int:
        max_dev = 0
        steps = 0
        for i in nums:
            dev = 0
            while i != 0:
                if i % 2 == 0:
                    i = i / 2
                    dev = dev + 1
                else:
                    i = i - 1
                    steps = steps + 1
            if dev > max_dev:
                max_dev = dev
        return steps + max_dev
