class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 求两球之间的最小最大值
        position.sort()
        l, r = 0, position[-1] - position[0]  # 两球之间的距离
        while l < r:
            mid = (l + r + 1) // 2
            count = 1
            last = position[0]
            for a in position[1:]:
                if a - last >= mid:
                    count += 1
                    last = a
            if count < m:
                r = mid - 1
            else:
                l = mid
        return l
