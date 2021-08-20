class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        (res, q, n, start) = (0, [], len(nums), 0)
        for (i, v) in enumerate(nums):
            if v == 0:
                start = i + 1
                q = []
            elif v < 0:
                q.append(i)
            if len(q) & 1:
                res = max(res, i - q[0], q[-1] - start)
            else:
                res = max(res, i - start + 1)
        return res
