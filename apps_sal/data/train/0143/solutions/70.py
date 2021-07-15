class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        c = collections.Counter()
        j = 0
        ans = 0
        for i in range(len(tree)):
            c[tree[i]]+=1
            while len(c)>=3:
                c[tree[j]] -= 1
                if c[tree[j]]==0:
                    del c[tree[j]]
                j+=1
            ans = max(ans,i-j+1)
        return ans
