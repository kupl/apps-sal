class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count, i, j = {}, 0, 0
        max_cnt = 0
        while j < len(tree):
            # print(count)
            v = tree[j]
            count[v] = count.get(v, 0) + 1
            if len(count) <= 2:
                max_cnt = max(sum(count.values()), max_cnt)
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            j += 1
        return max_cnt
                
        
# j = 2
# i = 1
# count = {
#     3: 2,
#     1: 1,
#     2: 1
# }

