class FenwickTree:

    def __init__(self, nums_node: int):
        self.nums_node = nums_node
        self.arr = [0] * nums_node
        self.total = 0

    def get_sum(self, index: int):
        if index < 0:
            return self.total - self.get_sum(~index)
        if index >= self.nums_node:
            return self.total
        result = 0
        while index >= 0:
            result += self.arr[index]
            index = (index & index + 1) - 1
        return result

    def update(self, index: int, delta: int):
        self.total += delta
        while index < self.nums_node:
            self.arr[index] += delta
            index = index | index + 1


class Solution:

    def numTeams(self, rating: list) -> int:
        count = 0
        rating_len = len(rating)
        sort_map = {r: i for (i, r) in enumerate(sorted(rating))}
        left_tree = FenwickTree(rating_len)
        right_tree = FenwickTree(rating_len)
        for rat in rating:
            right_tree.update(sort_map[rat], 1)
        for rat in rating:
            index = sort_map[rat]
            right_tree.update(index, -1)
            count += left_tree.get_sum(index) * right_tree.get_sum(~index)
            count += left_tree.get_sum(~index) * right_tree.get_sum(index)
            left_tree.update(index, 1)
        return count
