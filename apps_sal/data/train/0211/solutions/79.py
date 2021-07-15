class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        queue = [(set([s[:i]]), s[i:]) for i in range(1, len(s) + 1)]
        while queue:
            curSet, curS = queue.pop(0)
            if curS == '':
                ans = max(ans, len(curSet))

            for i in range(1, len(curS) + 1):
                if curS[:i] in curSet:
                    continue
                else:
                    tmpSet = curSet.copy()
                    tmpSet.add(curS[:i])
                    queue.append((tmpSet, curS[i:]))

        return ans
