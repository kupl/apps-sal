class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        i, maxLen = 0, 0
        cache = collections.defaultdict(int)
        for j in range(len(tree)):
            cache[tree[j]] += 1
            if len(cache) <= 2:
                maxLen = max(maxLen, j - i + 1)
            while len(cache) > 2:
                cache[tree[i]] -= 1
                if cache[tree[i]] == 0:
                    del cache[tree[i]]
                i += 1
        if maxLen == 0:
            return 1
        return maxLen
