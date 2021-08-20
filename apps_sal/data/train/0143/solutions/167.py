class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        store = collections.defaultdict(lambda: 0)
        ans = 0
        i = 0
        for (k, val) in enumerate(tree):
            store[val] += 1
            while len(store) > 2:
                store[tree[i]] -= 1
                if store[tree[i]] == 0:
                    del store[tree[i]]
                i += 1
            ans = max(ans, k - i + 1)
        return ans
