class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if not tree:
            return 0
        i = 0
        max_value = 0
        count = Counter()
        for index, value in enumerate(tree):
            count[value] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            max_value = max(max_value, index - i + 1)
        return max_value
