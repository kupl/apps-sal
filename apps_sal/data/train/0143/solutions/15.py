class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        i = 0
        count = collections.Counter()
        for (index, value) in enumerate(tree):
            count[value] += 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
        return len(tree) - i
