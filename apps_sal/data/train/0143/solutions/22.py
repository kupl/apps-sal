from collections import Counter


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        max_fruits = 0
        window_start = 0
        freq = Counter()
        for (i, val) in enumerate(tree):
            freq[val] += 1
            while len(freq) > 2:
                to_delete = tree[window_start]
                freq[to_delete] -= 1
                if not freq[to_delete]:
                    del freq[to_delete]
                window_start += 1
            max_fruits = max(max_fruits, i - window_start + 1)
        return max_fruits
