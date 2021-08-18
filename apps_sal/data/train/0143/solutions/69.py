
from collections import defaultdict


class Solution:
    def totalFruit(self, tree):
        if len(tree) < 3:
            return len(tree)
        best_pair = 0
        forest = defaultdict(int)
        forest[tree[0]] = (0, 1)
        for t in range(1, len(tree)):
            if tree[t] not in forest:
                best_pair = max([best_pair, sum([b for basket in list(forest.values()) for b in basket])])
                temp = defaultdict(int)
                temp[tree[t]] = (0, 0)
                temp[tree[t - 1]] = (0, forest[tree[t - 1]][-1])
                forest = temp
            if tree[t] == tree[t - 1]:
                forest[tree[t]] = (forest[tree[t]][0], forest[tree[t]][-1] + 1)
            else:
                forest[tree[t]] = (sum(forest[tree[t]]), 1)
        best_pair = max([best_pair, sum([b for basket in list(forest.values()) for b in basket])])
        return best_pair
