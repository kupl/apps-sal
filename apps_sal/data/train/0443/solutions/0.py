class Solution:
    def increment_index(self, nums, index):
        index += 1
        while index < len(nums):
            nums[index] += 1
            index += (index & -index)

    def prefix_sum(self, nums, index):
        index += 1
        current_sum = 0
        while index > 0:
            current_sum += nums[index]
            index -= (index & -index)
        return current_sum

    def numTeams(self, rating):
        if len(rating) < 3:
            return 0

        n = len(rating)
        sorted_nums = rating.copy()
        sorted_nums.sort()

        index = {}
        for i in range(n):
            index[sorted_nums[i]] = i

        fenwick_tree = [0] * (len(sorted_nums) + 1)

        lesser_before = [0] * n
        for i in range(n):
            rate_i = rating[i]
            index_i = index[rate_i]
            lesser_before[i] = self.prefix_sum(fenwick_tree, index_i)
            self.increment_index(fenwick_tree, index[rating[i]])

        for i in range(len(fenwick_tree)):
            fenwick_tree[i] = 0

        lesser_after = [0] * n
        for i in range(n - 1, -1, -1):
            rate_i = rating[i]
            index_i = index[rate_i]
            lesser_after[i] = self.prefix_sum(fenwick_tree, index_i)
            self.increment_index(fenwick_tree, index[rating[i]])

        num_teams = 0
        for i in range(n - 1):
            num_teams += lesser_before[i] * (n - 1 - i - lesser_after[i])
            num_teams += (i - lesser_before[i]) * lesser_after[i]

        return num_teams
