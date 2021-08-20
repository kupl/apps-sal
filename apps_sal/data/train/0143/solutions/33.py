class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        counter = {}
        res = 0
        for (j, v) in enumerate(tree):
            counter[v] = counter.get(v, 0) + 1
            while len(counter) > 2:
                counter[tree[i]] -= 1
                if not counter[tree[i]]:
                    del counter[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
