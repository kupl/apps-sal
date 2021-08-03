class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0
        dfs = [[set(), s]]
        while dfs:
            curSet, curS = dfs.pop()
            res = max(res, len(curSet))
            if len(curSet) + len(curS) <= res or len(curS) == 0:
                continue

            for i in range(len(curS)):
                if curS[:i + 1] in curSet:
                    continue

                curSet.add(curS[:i + 1])
                dfs.append([curSet.copy(), curS[i + 1:]])
                curSet.remove(curS[:i + 1])

        return res
