class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        dfs = [[set(), s]]
        while dfs:
            curEl = dfs.pop()
            res = max(res, len(curEl[0]))
            if len(curEl[0]) + len(curEl[1]) <= res or len(curEl[1]) == 0:
                continue
            for i in range(len(curEl[1])):
                noDel = curEl[1][:i + 1] in curEl[0]
                curEl[0].add(curEl[1][:i + 1])
                dfs.append([curEl[0].copy(), curEl[1][i + 1:]])
                if not noDel:
                    curEl[0].remove(curEl[1][:i + 1])
        return res
