# 思路
# 贪心策略，我们尽量找到能够覆盖最远（右边）位置的水龙头，并记录它最右覆盖的土地。

# 我们使用 furthest[i] 来记录经过每一个水龙头 i 能够覆盖的最右侧土地。
# 一共有 n+1 个水龙头，我们遍历 n + 1 次。
# 对于每次我们计算水龙头的左右边界，[i - ranges[i], i + ranges[i]]
# 我们更新左右边界范围内的水龙头的 furthest
# 最后从土地 0 开始，一直到土地 n ，记录水龙头数目


# 复杂度分析

# 时间复杂度：时间复杂度取决 l 和 r，也就是说取决于 ranges 数组的值，假设 ranges 的平均大小为 Size 的话，那么时间复杂度为 $O(N * Size)$。

# 空间复杂度：我们使用了 furthest 数组， 因此空间复杂度为 $O(N)$。


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        furthest, cnt, cur = [0] * n, 0, 0  # 做initialization

        for i in range(n + 1):
            l = max(0, i - ranges[i])  # 左边最远到哪里
            r = min(n, i + ranges[i])  # n是自己
            for j in range(l, r):  # 在左右两边，表示右边能到的最远的地方，
                furthest[j] = max(furthest[j], r)  # 经过这个水龙头最多能走到哪里，跟自己无关（没那么有关），跟经过我最远到哪里有关系
        while cur < n:  # 从头到尾扫一遍，看看有米有没灌溉到的地方
            if furthest[cur] == 0:
                return -1
            cur = furthest[cur]  # 比这个数值小的都是能扫到的部分，所以可以直接跳过去
            cnt += 1
        return cnt  # 左边有问题的话会-1
