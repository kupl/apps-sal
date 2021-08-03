def pos(mid, position, m):
    res = 1
    curr_pos = 0
    for i in range(1, len(position)):
        if position[i] - position[curr_pos] >= mid:
            curr_pos = i
            res += 1
            if res == m:
                return True
    return False


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 0
        h = position[-1] - position[0]
        res = 0
        while l <= h:
            mid = int((h + l) / 2)
            if pos(mid, position, m) == False:
                h = mid - 1
            else:
                res = max(res, mid)
                l = mid + 1
        return res
