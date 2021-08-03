class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) == 1:
            return 1
        start = last1 = last2 = 0
        res = 1
        for i in range(1, len(tree)):
            if tree[i] == tree[last1]:
                last1 = i
            elif tree[i] == tree[last2]:
                last2 = i
            elif tree[last1] == tree[last2]:
                last1 = max(last1, last2)
                last2 = i
            else:
                start = min(last1, last2) + 1
                if last1 < last2:
                    last1 = i
                else:
                    last2 = i
            res = max(res, i - start + 1)
        return res
