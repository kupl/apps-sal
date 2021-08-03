class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s, res = 'abc', []

        def dfs(s, length, path, res):
            if len(path) == length:
                res.append(path)
                return
            for i in range(len(s)):
                if path and s[i] == path[-1]:
                    continue
                else:
                    dfs(s, length, path + s[i], res)

        dfs(s, n, '', res)
        res.sort()
        # print(res)
        return res[k - 1] if k <= len(res) else ''
