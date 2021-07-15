from collections import defaultdict

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # freq = defaultdict(int)
        # freq[2] += 1
        # ftypes = set()
        # ftypes.add(2)
        
        if not tree:
            return 0
        
        freq, ftypes, ans, i = defaultdict(int), set(), float('-inf'), 0
        
        for j, num in enumerate(tree):
            freq[num] += 1
            ftypes.add(num)
            
            while len(ftypes) > 2:
                freq[tree[i]] -= 1
                if freq[tree[i]] == 0:
                    ftypes.remove(tree[i])
                i += 1
            
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans
