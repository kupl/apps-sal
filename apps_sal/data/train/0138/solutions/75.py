def f(data):
    n2 = len(data)
    f0 = -1
    f1 = -1
    n = 0
    for (ind, d) in enumerate(data):
        if d == 1:
            continue
        n += 1
        if f0 == -1:
            f0 = ind
        f1 = ind
    if n & 1 == 0:
        return n2
    return max(f1, n2 - f0 - 1)


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        res = 0
        prev = -1
        data = []
        for (ind, num) in enumerate(nums):
            if num == 0:
                if data:
                    res = max(res, f(data))
                prev = ind
                data = []
                continue
            data.append(1 if num > 0 else -1)
        res = max(res, f(data))
        return res
