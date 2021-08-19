class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        basket1 = -1
        basket2 = -1
        max_fruit = 0
        start = 0
        end = 0
        i = 0
        while i < len(tree):
            if tree[i] == basket1 or tree[i] == basket2:
                if tree[i] != tree[i - 1]:
                    end = i
                i += 1
                continue
            if basket1 == -1:
                basket1 = tree[i]
                end = i
                i += 1
                continue
            if basket2 == -1:
                basket2 = tree[i]
                end = i
                i += 1
                continue
            print(i)
            print(end)
            weight = i - start
            max_fruit = max(max_fruit, weight)
            i = end
            start = end
            basket1 = -1
            basket2 = -1
        weight = len(tree) - start
        max_fruit = max(max_fruit, weight)
        return max_fruit
