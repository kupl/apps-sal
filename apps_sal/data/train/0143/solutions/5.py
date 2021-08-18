class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        maxi = 0
        if len(tree) == 1:
            return 1
        l = []
        s = set()
        for i in range(len(tree)):
            l.append(tree[i])
            s.add(tree[i])
            if len(s) > 2:
                while len(set(l)) > 2:
                    l = l[1:]
            maxi = max(maxi, len(l))
        return maxi
