class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        (idx, baskets, res) = (-1, collections.deque(maxlen=2), 0)
        for (i, x) in enumerate(tree):
            if x not in [y[0] for y in baskets]:
                if len(baskets) == 2:
                    (res, idx) = (max(res, i - idx - 1), baskets[0][1])
                baskets.append([x, i])
            elif x == baskets[0][0]:
                baskets.popleft()
                baskets.append([x, i])
            else:
                baskets[1][1] = i
        return max(res, len(tree) - 1 - idx)
