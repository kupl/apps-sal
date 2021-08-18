import math


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        n = len(arr)
        arr.sort()

        def get_candidates(sm, k, l, r):
            if k == 0:
                yield abs(sm - target), l
            else:
                y = math.floor((target - sm) / k)
                for x in [y, y + 1]:
                    x = max(l, min(r, x))
                    yield abs(sm + k * x - target), x

        def get_segments():
            sm = 0
            for i in range(n):

                l = 0 if i == 0 else arr[i - 1]
                r = arr[i] - 1

                if l <= r:
                    yield sm, n - i, l, r

                sm += arr[i]

            yield sm, 0, arr[-1], int(1e9)

        return min((xd for t in get_segments() for xd in get_candidates(*t)))[1]
