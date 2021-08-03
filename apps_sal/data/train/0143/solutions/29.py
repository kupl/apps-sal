class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree or len(tree) == 0:
            return 0
        max_ = 1
        mem = {}
        i, j = 0, 0
        while j < len(tree):
            if len(mem) <= 2:
                mem[tree[j]] = j
                j += 1
            if len(mem) > 2:
                min_ = len(tree) - 1
                for value in mem.values():
                    min_ = min(min_, value)
                i = min_ + 1
                del mem[tree[min_]]
            max_ = max(max_, j - i)

        return max_
