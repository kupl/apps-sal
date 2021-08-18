class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 1

        tree_nums = [0] * (n + 1)
        tree_nums[0] = 1
        tree_nums[1] = 1

        for t in range(2, n + 1):
            for root in range(1, t + 1):
                lt_num = root - 1
                rt_num = t - root

                tree_nums[t] += tree_nums[lt_num] * tree_nums[rt_num]

        return tree_nums[n]
