class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # dp 一定超时
        # minimax的题目，基本上都是binary search + greedy helper function
        # 用count(d)表示：当最小的距离是d时，最多能够放的球的个数，目标就是去找count(d)==m时，最大的d
        # 用二分思想:
        # 当count(d)<m时，说明d太大了，有的球放不下
        # 当count(d)>m时，说明d太小了，还有更多的球能放

        position.sort()

        l = 1
        r = position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if self.helper(mid, position) >= m:
                l = mid
            else:
                r = mid - 1

        return l

    def helper(self, d, position):
        res = 1
        cur = position[0]
        for i in range(1, len(position)):
            if position[i] - cur >= d:
                cur = position[i]
                res += 1
        return res
