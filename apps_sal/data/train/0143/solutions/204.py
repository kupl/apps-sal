class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        cnt = collections.Counter()
        i = 0
        res = 0
        for j in range(len(tree)):
            cnt[tree[j]] += 1
            while len(cnt) > 2:
                cnt[tree[i]] -= 1
                if cnt[tree[i]] == 0:
                    cnt.pop(tree[i])
                i += 1
            res = max(res, sum(cnt.values()))
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # fruit_1, fruit_2 = None, None
        # pos_1, pos_2 = -1, -1
        # i = 0
        # max_len = 0
        # for t in range(len(tree)):
        #     if tree[t]==fruit_1:
        #         fruit_1, fruit_2 = fruit_2, fruit_1
        #         pos_1, pos_2 = pos_2, t
        #     elif tree[t]==fruit_2:
        #         pos_2 = t
        #     else:
        #         fruit_1, fruit_2 = fruit_2, tree[t]
        #         i = pos_1 + 1
        #         pos_1, pos_2 = pos_2, t
        #     if t - i + 1 > max_len:
        #         max_len = t - i + 1
        # return max_len

