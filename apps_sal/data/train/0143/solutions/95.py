class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        a = Counter(tree)
        if len(a) <= 2:
            return len(tree)
        ans = 0
        i = 0
        while i < len(tree):
            count = 1
            basket = [tree[i]]
            j = i + 1
            while j < len(tree):
                if tree[j] in basket:
                    count += 1
                elif len(basket) >= 2:
                    break
                else:
                    basket.append(tree[j])
                    count += 1
                j += 1
            if count > ans:
                ans = count
            i += 1
        return ans
