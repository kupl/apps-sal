class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        k = 2
        left = 0
        cnt = collections.Counter()
        res = 0
        for j, i in enumerate(tree):
            if cnt[i] == 0: k-=1
            cnt[i] += 1
            while k<0:
                cnt[tree[left]] -= 1
                if cnt[tree[left]] == 0: k+=1
                left += 1
            res = max(res, j-left +1)
        return res
            

