from collections import defaultdict


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counter = {}
        longest = 0
        fruits = 0
        i = 0
        for j in range(len(tree)):
            if tree[j] not in counter:
                fruits += 1
                counter[tree[j]] = 0
            counter[tree[j]] += 1
            while fruits > 2:
                counter[tree[i]] -= 1
                if counter[tree[i]] == 0:
                    fruits -= 1
                    del counter[tree[i]]
                i += 1
            longest = max(longest, j - i + 1)
        return longest
