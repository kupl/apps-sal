from functools import lru_cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        lim = len(arr)

        @lru_cache(None)
        def r(i):

            tmp = [0]
            for j in range(i - 1, i - d - 1, -1):
                if j < 0:
                    break
                if arr[j] < arr[i]:
                    tmp.append(1 + r(j))
                else:
                    break

            for j in range(i + 1, i + d + 1):
                if j >= lim:
                    break
                if arr[j] < arr[i]:
                    tmp.append(1 + r(j))
                else:
                    break

            return max(tmp)

        mx = 0
        for i in range(0, lim):
            val = 1 + r(i)
            if val > mx:
                mx = val

        return mx
