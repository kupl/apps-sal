class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(x: int):
            pre = position[0]
            num = 1
            for ii in range(1, N):
                if position[ii] - pre >= x:
                    pre = position[ii]
                    num += 1
            return num >= m
        N = len(position)
        position = sorted(position)
        (left, right, res) = (0, position[-1] - position[0], -1)
        while left <= right:
            mid = left + right >> 1
            if check(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res
