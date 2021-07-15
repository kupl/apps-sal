from collections import Counter
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        d = Counter()
        left = 0 
        total = 0
        for idx, i in enumerate(tree):
            d[i] += 1 
            while(len(d) > 2):
                d[tree[left]] -= 1 
                if(d[tree[left]] == 0):
                    del d[tree[left]]
                left += 1 
                
            total = max(total, idx - left + 1)
        return total

