class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, res, check = 0, 0, dict()
        for i, t in enumerate(tree):
            check[t] = check.get(t, 0) + 1
            if len(check) <= 2:
                res = max(res, i - l + 1)
            while len(check) > 2:
                check[tree[l]] -= 1
                if check[tree[l]] == 0:
                    del check[tree[l]]
                l += 1
        return res
