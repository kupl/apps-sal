class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
#         winstart=0
#         maxlen=0
#         for winend in range(len(tree)+1):
#             while(len(set(tree[winstart:winend])))>=3:
#                 winstart+=1
#             maxlen=max(maxlen,winend - winstart)
            
#         return maxlen
                
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
