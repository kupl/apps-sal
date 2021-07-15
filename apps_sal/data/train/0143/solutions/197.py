# 问题可以抽象为给定一个数组，求解最多选择两种数字的情况下，最大的连续子序列长度，其中数组和原题目一样，每一个数字代表一个水果。

# 我们可以使用滑动窗口来解决。 思路和 【1004. 最大连续 1 的个数 III】滑动窗口（Python3） 一样。



class Solution:
    def atMostK(self, nums, K):
        counter = collections.Counter()
        res = i = 0
        for j in range(len(nums)):
            if counter[nums[j]] == 0:
                K -= 1
            counter[nums[j]] += 1  #然后加上1
            while K < 0:
                counter[nums[i]] -= 1  #移去最外面的，然后自己往左走
                if counter[nums[i]] == 0:
                    K += 1  #说明有一个品种多出来了，所以在没有到可以移出品种之前，需要一直变动
                i += 1
            res = max(res, j - i + 1)  #因为还要多一个
        return res

    def totalFruit(self, tree: List[int]) -> int:
        return self.atMostK(tree, 2)   #最多两个

# 复杂度分析

# 时间复杂度：O(N)O(N)
# 空间复杂度：O(N))O(N)) （我们使用了Counter）

