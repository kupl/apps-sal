class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        cnt = 1
        max = 1
        keys = set([tree[0]])
        spree = [tree[0], 1]
        for k in range(1, len(tree)):
            if tree[k] in keys:
                cnt += 1
                if tree[k] == spree[0]:
                    spree[1] += 1
                else:
                    spree = [tree[k], 1]
            elif len(keys) == 1:
                keys.add(tree[k])
                cnt += 1
                spree = [tree[k], 1]
            else:
                if cnt > max:
                    max = cnt
                keys = set([tree[k - 1], tree[k]])
                cnt = spree[1] + 1
                spree = [tree[k], 1]
        if cnt > max:
            max = cnt
        return max
