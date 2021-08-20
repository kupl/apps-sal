class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        ans = i = 0
        freq = collections.defaultdict(int)
        for (j, fruit) in enumerate(tree):
            freq[fruit] += 1
            while len(freq) == 3:
                freq[tree[i]] -= 1
                if freq[tree[i]] == 0:
                    del freq[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
