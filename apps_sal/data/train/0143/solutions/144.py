class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l = 0
        count = {}

        for r, value in enumerate(tree):
            count[value] = count.get(value, 0) + 1
            if len(count) > 2:
                count[tree[l]] -= 1
                if count[tree[l]] == 0:
                    del count[tree[l]]
                l += 1

        return r - l + 1
