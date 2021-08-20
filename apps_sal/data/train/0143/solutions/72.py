class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        current_picking = tree[0]
        prev_picking = None
        max_picked = 0
        baskets = {current_picking: [0, 0]}
        for i in range(len(tree)):
            if tree[i] != current_picking:
                if len(baskets) < 2:
                    baskets[current_picking] = [0, i - 1]
                    prev_picking = current_picking
                    current_picking = tree[i]
                    baskets[current_picking] = [i, i]
                elif tree[i] != prev_picking:
                    baskets = {current_picking: [baskets[prev_picking][1] + 1, baskets[current_picking][1]], tree[i]: [i, i]}
                    prev_picking = current_picking
                    current_picking = tree[i]
                else:
                    (prev_picking, current_picking) = (current_picking, prev_picking)
                    baskets[current_picking][1] = i
            else:
                baskets[current_picking][1] = i
            if baskets.get(current_picking) and baskets.get(prev_picking):
                max_picked = max(max_picked, max([pos[1] for pos in baskets.values()]) - min([pos[0] for pos in baskets.values()]) + 1)
            else:
                max_picked = max(max_picked, baskets[current_picking][1] - baskets[current_picking][0] + 1)
        return max_picked
