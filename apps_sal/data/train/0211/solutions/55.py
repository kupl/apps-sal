class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        currli = []
        visiting = set()
        self.maxval = 1

        def dfs(st, s):
            if len(s) <= 0:
                self.maxval = max(self.maxval, len(currli))
                return True
            for i in range(1, len(s) + 1):
                if s[0:i] not in visiting:
                    visiting.add(s[0:i])
                    currli.append(s[0:i])
                    dfs(i, s[i:])
                    currli.pop()
                    visiting.remove(s[0:i])
            return False
        for i in range(1, n + 1):
            visiting.add(s[0:i])
            currli.append(s[0:i])
            dfs(i, s[i:])
            currli.pop()
            visiting.remove(s[0:i])
        return self.maxval
