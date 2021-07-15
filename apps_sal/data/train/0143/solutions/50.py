class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(j - i + 1, ans)
        return ans
