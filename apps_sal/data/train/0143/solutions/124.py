import collections
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res=i=0
        count=Counter()
        for j, k in enumerate(tree):
            count[tree[j]] +=1
            while len(count)>=3:
                count[tree[i]] -= 1
                if count[tree[i]]==0:
                    del count[tree[i]]
                i +=1
            res=max(res, j-i+1)
        return res
