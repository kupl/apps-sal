class Solution:

    def getHappyString(self, n: int, k: int) -> str:

        def dfs(ind, nlen, path, res):
            if ind == nlen:
                res.append(path)
                return
            for i in range(3):
                if len(path) == 0 or path[-1] != ls[i]:
                    dfs(ind + 1, nlen, path + ls[i], res)
        ls = ['a', 'b', 'c']
        vis = [0] * 3
        res = []
        dfs(0, n, '', res)
        res.sort()
        if len(res) < k:
            return ''
        return res[k - 1]
