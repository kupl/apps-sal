class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        count = collections.Counter()
        j = res = 0
        for i in range(len(tree)):
            count[tree[i]] += 1
            while len(count) > 2:
                count[tree[j]] -= 1
                if count[tree[j]] == 0:
                    del count[tree[j]]
                j += 1
            res = max(res, sum(count.values()))
        return res
