class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = 0
        starts = {}
        start = end = 0
        longest = 0

        def find_earliest(starts):
            earliest = len(tree)
            for key in starts:
                earliest = min(starts[key], earliest)
            return earliest

        while end < len(tree):
            current = tree[end]
            if current in starts:
                starts[current] = end
                end += 1
            else:
                if counts == 2:
                    earliest = find_earliest(starts)
                    del starts[tree[earliest]]
                    start = earliest + 1
                    counts -= 1
                else:
                    starts[current] = end
                    counts += 1
                    end += 1
            longest = max(end - start, longest)

        return max(end - start, longest)
