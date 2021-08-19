class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 2:
            return len(tree)
        types = {tree[0]: 0, tree[1]: 1} if tree[0] != tree[1] else {tree[0]: 1}
        res = 2
        temp = 2
        for i in range(2, len(tree)):
            if len(types) == 2:
                if tree[i] not in types:
                    res = max(res, temp)
                    delete = sorted(types, key=types.get)[0]
                    temp = i - types[delete]
                    del types[delete]
                    types[tree[i]] = i
                else:
                    temp += 1
                    types[tree[i]] = i
            else:
                temp += 1
                types[tree[i]] = i
        res = max(res, temp)
        return res
