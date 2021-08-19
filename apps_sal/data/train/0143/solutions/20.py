class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        start = 0
        max = 0
        reset = 0
        baskets = {1: [None, 0], 2: [None, 0]}
        while start < len(tree) and start >= 0:
            if baskets[1][0] == None:
                baskets[1][0] = tree[start]
                baskets[1][1] += 1
                while reset and start > 0:
                    if baskets[1][0] != tree[start - 1]:
                        reset = 0
                    else:
                        start -= 1
            elif baskets[1][0] == tree[start]:
                baskets[1][1] += 1
            elif baskets[2][0] == None:
                baskets[2][0] = tree[start]
                baskets[2][1] += 1
            elif baskets[2][0] == tree[start]:
                baskets[2][1] += 1
            else:
                if max < baskets[1][1] + baskets[2][1]:
                    print((baskets, start))
                baskets = {1: [None, 0], 2: [None, 0]}
                reset = 1
            if reset == 1:
                if start > 0:
                    start -= 1
            else:
                start += 1
            if max < baskets[1][1] + baskets[2][1]:
                max = baskets[1][1] + baskets[2][1]
        return max
