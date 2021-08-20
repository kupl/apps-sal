class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        have = set()
        self.cur = []

        def dfs(i):
            if i == len(s):
                return 0 if ''.join(self.cur) not in have else -float('inf')
            self.cur.append(s[i])
            ret = dfs(i + 1)
            st = ''.join(self.cur)
            if st not in have:
                (tmp, self.cur) = (self.cur, [])
                have.add(st)
                ret = max(dfs(i + 1) + 1, ret)
                have.remove(st)
                self.cur = tmp
            self.cur.pop()
            return ret
        return dfs(0)
