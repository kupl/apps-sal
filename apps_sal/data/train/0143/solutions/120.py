class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = []
        ind = 0
        if len(tree) == 1:
            return 1
        if len(set(tree)) <= 2:
            return len(tree)
        while ind < len(tree) - 1:
            count = 0
            types = set()
            for i in range(ind, len(tree)):
                types.add(tree[i])
                if len(types) > 2:
                    break
                count += 1
            res.append(count)
            ind += 1
        return max(res)
