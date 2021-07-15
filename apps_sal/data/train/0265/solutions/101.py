class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        s = {0}
        res = 0
        cur = 0
        for x in nums:
            cur += x
            if cur - target in s:
                #print(x)
                res += 1
                cur = 0
                s = {0}
                continue
            s.add(cur)
        return res
