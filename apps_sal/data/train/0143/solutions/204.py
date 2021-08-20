class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        cnt = collections.Counter()
        i = 0
        res = 0
        for j in range(len(tree)):
            cnt[tree[j]] += 1
            while len(cnt) > 2:
                cnt[tree[i]] -= 1
                if cnt[tree[i]] == 0:
                    cnt.pop(tree[i])
                i += 1
            res = max(res, sum(cnt.values()))
        return res
