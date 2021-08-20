class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        maxCol = 0
        baskets = [0, 0]
        while i < len(tree) and maxCol + i < len(tree):
            baskets[0] = tree[i]
            j = i + 1
            basket1Empty = True
            while j < len(tree):
                if tree[j] != baskets[0] and basket1Empty:
                    baskets[1] = tree[j]
                    basket1Empty = False
                elif tree[j] != baskets[0] and tree[j] != baskets[1]:
                    col = j - i
                    if col > maxCol:
                        maxCol = col
                    break
                j += 1
            col = j - i
            if col > maxCol:
                maxCol = col
            i += 1
        return maxCol
