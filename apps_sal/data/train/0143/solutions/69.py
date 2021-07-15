
from collections import defaultdict
class Solution:
    def totalFruit(self, tree):
        if len(tree) <3:
            return len(tree)
        # run1 = 0
        # run2 = 1
        # # run3 = 0
        best_pair = 0
        # tree_type1 = None
        # tree_type2 = tree[0]
        forest = defaultdict(int)
        forest[tree[0]] = (0,1)
        for t in range(1, len(tree)):
            # print('tree',t)
            if tree[t] not in forest:
                best_pair = max([best_pair, sum([b for basket in list(forest.values()) for b in basket])])
                temp = defaultdict(int)
                temp[tree[t]] = (0,0)
                temp[tree[t-1]] = (0,forest[tree[t-1]][-1])
                forest = temp
                # print('established tt1', t)
            if tree[t] == tree[t-1]:
                forest[tree[t]] = (forest[tree[t]][0],forest[tree[t]][-1]+1)
            else:
                # print(forest)
                forest[tree[t]] = (sum(forest[tree[t]]),1)
            # if t == tree_type1:
            #     run1 += 1
            #     print('run1',run1)
            # elif t == tree_type2:
            #     run2 += 1
            #     print('run2', run2)
            # else:
            #     print('new set')
            #     best_pair = max([best_pair, sum([run1, run2])])
            #     run2 = run1
            #     run1 = 1
            #     tree_type2 = tree_type1
            #     tree_type1 = t
            #     print(best_pair, run1, run2, 'tree_type1',tree_type1,'tree_type2', tree_type2)
            # print(run1, run2)
            # print(forest)
            # print(best_pair)
        best_pair = max([best_pair, sum([b for basket in list(forest.values()) for b in basket])])
        return best_pair

