import numpy as np
import itertools as it


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        arr = np.sort(position)
        arr = arr - np.min(arr)
        print(arr)

        def isFeasible(mid, arr, m):
            pos = arr[0]
            n = len(arr)
            count = 1
            for i in range(n):
                if arr[i] - pos >= mid:
                    pos = arr[i]
                    count += 1
                if count >= m:
                    return True
            return False

        left = arr[0]
        right = arr[-1]

        if m == 2:
            return right - left
        res = -1
        count = 0
        while left < right:
            mid = (right + left) // 2
            count += 1
            if isFeasible(mid, arr, m):
                res = max(res, mid)
                left = mid + 1

            else:
                right = mid
        print(count)
        return int(res)
