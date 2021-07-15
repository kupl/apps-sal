from collections import Counter

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets = Counter()
        max_fr = 0
        i = 0
        
        for j, t in enumerate(tree):
            baskets[t] += 1
            
            while len(baskets) > 2:
                baskets[tree[i]] -= 1
                if baskets[tree[i]] == 0:
                    del baskets[tree[i]]
                
                i += 1
            
            max_fr = max(max_fr, j - i + 1)
        
        return max_fr

# class Solution:

#     def totalFruit(self, tree):
#         count, i = {}, 0
#         for j, v in enumerate(tree):
#             count[v] = count.get(v, 0) + 1
#             if len(count) > 2:
#                 count[tree[i]] -= 1
#                 if count[tree[i]] == 0: del count[tree[i]]
#                 i += 1
#         return j - i + 1

