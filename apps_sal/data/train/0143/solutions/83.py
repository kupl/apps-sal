class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 2:
            return len(tree)

        n = len(tree)

        res = 0
        start = 0
        while start < n:
            type1, type2, type2_pos = -1, -1, -1
            i = start
            while i < n:
                if type1 == -1:
                    type1 = tree[i]

                elif tree[i] != type1 and type2 == -1:
                    type2 = tree[i]
                    type2_pos = i

                elif tree[i] != type1 and tree[i] != type2:
                    break
                i += 1

            res = max(res, i - start)
            if i == n:
                break
            start = type2_pos

        return res
