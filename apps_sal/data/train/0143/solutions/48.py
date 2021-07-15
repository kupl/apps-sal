class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) < 2: return len(tree)
        start, end, res = 0, 1, 1
        basket = {tree[start]: 1}
        while end < len(tree):
            if tree[end] in basket:
                basket[tree[end]] +=1
                end += 1
                res = max(res, end-start)
            elif len(basket) < 2:
                basket[tree[end]] = 1
                end += 1
                res = max(res, end-start)
            else:
                basket[tree[start]] -= 1
                if basket[tree[start]] == 0:
                    del basket[tree[start]]
                start += 1
        return res
