class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        t1 = t2 = -1
        t1s = -1
        ans = 0;
        for i in range(0, len(tree)):
            t = tree[i]
            if t != t1 and t != t2:
                ans = max(ans, i - t1s)
                t1s = i
                while (t1s > 0 and tree[t1s - 1] == tree[i - 1]):
                    t1s -= 1
                t1 = tree[i - 1]
                t2 = t
        ans = max(ans, len(tree) - t1s)
        return ans
