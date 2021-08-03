class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        k = k - 1

        def dfs(path, new):

            if len(path) == n:
                res.append(path)
                return

            if len(path) == 0:
                for ind, x in enumerate(new):
                    dfs(path + x, new[:ind] + new[ind + 1:])

            else:
                last = path[-1]
                l = []
                for i in letters:
                    if i != last:
                        l.append(i)

                for ind, x in enumerate(l):
                    dfs(path + x, l[:ind] + l[ind + 1:])

        letters = ['a', 'b', 'c']
        res = []
        dfs('', letters)

        if k >= len(res):
            return ''
        else:
            return res[k]
