class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        max_ = 0
        baskets = {}

        def get_other_tree(this_tree):
            trees = list(baskets.keys())
            return trees[1 - trees.index(this_tree)] if len(trees) == 2 else trees[0]
        for (idx, tr) in enumerate(tree):
            if tr not in baskets and len(baskets) == 2:
                max_ = max(max_, sum((sum(baskets[b]) for b in baskets)))
                last_tree = tree[idx - 1]
                other_tree = get_other_tree(last_tree)
                baskets = {last_tree: [baskets[last_tree][1], 0], tr: [0, 1]}
            else:
                there_is_another_tree = tr not in baskets and len(baskets) == 1 or (tr in baskets and len(baskets) == 2)
                if there_is_another_tree:
                    other_tree = get_other_tree(tr)
                    baskets[other_tree] = [sum(baskets[other_tree]), 0]
                if tr not in baskets:
                    baskets[tr] = [0, 0]
                baskets[tr][1] += 1
        return max(max_, sum((sum(baskets[b]) for b in baskets)))
