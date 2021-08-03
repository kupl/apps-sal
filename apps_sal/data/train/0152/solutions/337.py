class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        def helper(pos, mid, k):
            temp = pos[0]
            done = 1
            for i in range(1, len(pos)):
                if pos[i] - temp >= mid:
                    temp = pos[i]
                    done += 1
                if done == k:
                    return True

            return False

        position.sort()
        res = -1
        l, r = 0, position[-1]

        while l < r:
            mid = l + (r - l) // 2
            if helper(position, mid, m):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid

        return res
