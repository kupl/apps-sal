class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        (s, r) = divmod(sum(nums), p)
        if r == 0:
            return 0
        if s == 0:
            return -1
        result = len(nums)
        lastRems = {0: -1}
        x = 0
        cr = p - r
        for (i, nextX) in enumerate(nums):
            nextX = nextX % p
            x = (x + nextX) % p
            try:
                test = i - lastRems[(cr + x) % p]
                if test < result:
                    result = test
            except KeyError:
                pass
            lastRems[x] = i
        if result >= len(nums):
            return -1
        else:
            return result
