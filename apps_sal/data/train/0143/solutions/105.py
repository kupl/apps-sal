class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        c = 0
        p = 0
        for i in range(len(tree)):
            l = []
            k = 0
            for j in range(i, len(tree)):
                if(tree[j] not in l):
                    l.append(tree[j])
                    k += 1
                else:
                    k += 1
                if(len(l) > 2):
                    k = k - 1
                    break

            if(k > p):
                p = k
            if(p == len(tree)):
                break
        return p
