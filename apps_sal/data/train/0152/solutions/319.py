class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        high = int((position[-1] - position[0]) / (m - 1))
        low = 0
        while high - 1 > low:
            mid = int((high + low) / 2)
            if self.helper(position, mid, m):
                low = mid
            else:
                high = mid - 1
        if self.helper(position, high, m):
            return high
        else:
            return low

    def helper(self, position, max_d, m):
        count = 1
        pre_ind = 0
        ind = 1
        while ind < len(position):
            if count >= m:
                break
            if position[ind] - position[pre_ind] < max_d:
                ind += 1
            else:
                pre_ind = ind
                ind += 1
                count += 1
        if count >= m:
            return True
        else:
            return False
