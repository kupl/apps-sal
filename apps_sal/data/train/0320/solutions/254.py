class Solution:

    def minOperations(self, nums: List[int]) -> int:
        res = 0
        a = [x for x in nums if x]
        while a:
            for (i, x) in enumerate(a):
                if x & 1:
                    a[i] -= 1
                    res += 1
            a = [x // 2 for x in a if x]
            if a:
                res += 1
        return res
