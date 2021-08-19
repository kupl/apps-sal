class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        q = []
        ans = -99999999999
        s = 0
        e = s
        while e < len(tree):
            if tree[e] not in q:
                if len(q) < 2:
                    q.append(tree[e])
                else:
                    if e - s > ans:
                        ans = e - s
                    i = e - 1
                    while tree[i] == tree[e - 1] and i > -1:
                        i -= 1
                    s = i + 1
                    q.clear()
                    q.append(tree[s])
                    q.append(tree[e])
            e += 1
        if e - s > ans:
            ans = e - s
        return ans
