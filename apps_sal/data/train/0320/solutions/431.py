
def ops(x):
    if x == 1:
        return (0, 1)
    if x % 2 == 0:
        d, i = ops(x // 2)
        return (d + 1, i)
    else:
        d, i = ops(x - 1)
        return (d, i + 1)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        increments = 0
        max_doubles = 0

        for x in nums:
            if x == 0:
                continue
            doubs, incrs = ops(x)
            increments += incrs
            if doubs > max_doubles:
                max_doubles = doubs

        return increments + max_doubles


