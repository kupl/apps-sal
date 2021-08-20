class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        counter = collections.Counter()
        l = r = 0
        res = 0
        while r < len(tree):
            counter[tree[r]] += 1
            while len(counter.keys()) > 2:
                counter[tree[l]] -= 1
                if counter[tree[l]] == 0:
                    del counter[tree[l]]
                l += 1
            res = max(res, sum(counter.values()))
            r += 1
        return res
