class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 小心地使用暴力法求解: 可以尝试所有可能的间距, 找到最大的值
        # 两个观察:
        # 1. 要达到最优解第一个球一定放在第一个篮子里
        # 2. 如果最小间距为x时无法摆下所有球, 那么比x大的间距(x+1, x+2...)也不可能摆下所有球
        # 使用二分查找, 搜索能摆下所有球的间距
        # 需要确定: 二分查找的范围, 要满足的条件是啥
        # 二分查找模板->cond(k)成立的情况下最大化k
        position.sort()
        lo = 1
        # 显然最大间距不会超过这个值
        hi = position[-1] - position[0]
        while lo < hi:
            # 往右偏移的mid(corner case: lo=3, hi=4)
            mid = (lo + hi + 1) // 2
            if self.check(position, mid, m):
                lo = mid
            else:
                # mid不能满足条件
                hi = mid - 1
        # 当退出循环时hi是满足条件的最大值
        return hi

    # 检查最小间距为x时是否能放下所有的球
    def check(self, pos, x, m):
        remain_ball = m - 1  # 第一个球就放在第一个篮子里了
        n = len(pos)
        prev = 0
        for i in range(1, n):
            if pos[i] - pos[prev] >= x:
                remain_ball -= 1
                prev = i
                if remain_ball == 0:
                    return True
            else:
                continue
        return False
