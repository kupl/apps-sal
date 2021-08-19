import bisect


def calc(val, arr, prefix):
    i = bisect.bisect_left(arr, val)
    return prefix[i] + (len(arr) - i) * val


class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        prefix = [0]
        for (i, a) in enumerate(arr):
            prefix.append(prefix[i] + a)
        (l, h) = (0, arr[-1])
        if h * len(arr) <= target:
            return h
        while l < h - 1:
            m = (l + h) // 2
            curr = calc(m, arr, prefix)
            if curr >= target:
                h = m
            else:
                l = m
        l_d = abs(target - calc(l, arr, prefix))
        h_d = abs(target - calc(h, arr, prefix))
        if l_d <= h_d:
            return l
        else:
            return h
