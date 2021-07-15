class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = i = 0
        count = collections.defaultdict(int)
        for j, ftype in enumerate(tree):
            count[ftype] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    count.pop(tree[i])
                i += 1
            ans = max(ans, j - i + 1)
        return ans
