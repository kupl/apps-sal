class Solution:
    # https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/803580/Python-Solution-or-Binary-Search
    def maxDistance(self, position: List[int], m: int) -> int:
        def getBallCount(position, force):
            # res starts from 1, since we put one ball at index = 0.
            res, prev = 1, 0
            for i in range(1, len(position)):
                if position[i] - position[prev] >= force:
                    res += 1
                    prev = i
            return res

        position.sort()
        if m == 2:
            return position[-1] - position[0]
        l, r, res = 0, position[-1] + 1, 0
        while l < r:
            mid = l + (r - l) // 2
            # force is too small
            if getBallCount(position, mid) >= m:
                l = mid + 1
                # record res
                res = mid
            else:
                r = mid
        # return res, not l.
        return res
