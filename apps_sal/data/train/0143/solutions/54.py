class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count2 = 0
        basket = 0
        ans = 0
        kind1, kind2 = 0, 0
        for t in tree:
            if t == kind2:
                count2 += 1
                basket += 1
            elif t == kind1:
                count2 = 1
                basket += 1
                kind1, kind2 = kind2, kind1
            else:
                basket = count2 + 1
                count2 = 1
                kind1, kind2 = kind2, t
            ans = max(ans, basket)
        return ans

