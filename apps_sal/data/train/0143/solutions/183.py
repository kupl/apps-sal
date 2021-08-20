class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        block = []
        prev = tree[0]
        start = 0
        for i in range(1, len(tree)):
            if prev != tree[i]:
                block.append((prev, i - start))
                start = i
                prev = tree[i]
        block.append((prev, len(tree) - start))
        (head, tail) = (0, 1)
        basket = {block[0][0]: block[0][1]}
        res = block[0][1]
        while tail < len(block):
            (t, q) = block[tail]
            if t in list(basket.keys()):
                basket[t] += q
            elif len(basket) < 2:
                basket[t] = q
            else:
                while len(basket) == 2:
                    (ht, hq) = block[head]
                    head += 1
                    basket[ht] -= hq
                    if basket[ht] == 0:
                        basket.pop(ht)
                basket[t] = q
            val = 0
            for tt in list(basket.keys()):
                val += basket[tt]
            res = max(res, val)
            tail += 1
        return res
