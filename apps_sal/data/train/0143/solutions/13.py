class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans, j = 0, 0
        n = len(tree)
        dic = {}
        for i in range(n):
            dic[tree[i]] = i
            if len(dic) > 2:
                ans = max(ans, i - j)
                k = None
                for key in dic:
                    if key != tree[i] and key != tree[i - 1]:
                        k = key
                        j = dic[key] + 1
                del dic[k]

        return max(ans, n - j)
