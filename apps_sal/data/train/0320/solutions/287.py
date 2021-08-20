class Solution:

    def minOperations(self, nums: List[int]) -> int:
        delete_count = 0
        divide_count = 0
        for e in nums:
            divide = 0
            while e != 0:
                if e % 2:
                    e -= 1
                    delete_count += 1
                else:
                    e /= 2
                    divide += 1
            divide_count = max(divide_count, divide)
        return delete_count + divide_count
