class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        f1, f2= [-1,-1],[-1,-1]
        res, fruit1, fruit2 = 0, -1, -1
        for i in range(len(tree)):
            if tree[i] not in [fruit1,fruit2]:   
                if f2[1]>f1[1]:
                    f2[0] = f1[1]+1
                    f1 = [i,i]
                    fruit1 = tree[i]
                else:
                    f1[0] = f2[1]+1
                    f2 = [i,i]
                    fruit2 = tree[i]
            elif tree[i] == fruit1: f1[1] = i
            else: f2[1] = i
            res = max(res,max(f1[1],f2[1]) - min(f1[0],f2[0]))
        return res+1
