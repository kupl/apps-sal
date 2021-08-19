class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def countcall(x, c):
            c0 = 0
            for i in range(len(x)):
                if x[i] % 2 == 1:
                    c += 1
                    x[i] = (x[i] - 1) // 2
                else:
                    x[i] = x[i] // 2
                if x[i] == 0:
                    c0 += 1
            if c0 == len(x):
                return c
            else:
                c += 1
                return countcall(x, c)
        return countcall(nums, 0)
