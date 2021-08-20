class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        left = ans = 0
        types = collections.defaultdict(int)
        for right in range(len(tree)):
            types[tree[right]] += 1
            if len(types.keys()) <= 2:
                ans = max(ans, right - left + 1)
            while len(types.keys()) > 2:
                types[tree[left]] -= 1
                if types[tree[left]] == 0:
                    types.pop(tree[left])
                left += 1
        return ans
