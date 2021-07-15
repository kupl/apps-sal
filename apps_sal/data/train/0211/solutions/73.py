class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        if s  == None or len(s) == 0:
            return 0
        self.res = 0
        has = set()
        def dfs(cur, lasti, ct):
            if cur > len(s):
                self.res = max(self.res, ct)
                return
            for cur in range(cur, len(s) + 1):
                if s[lasti : cur] not in has:
                    has.add(s[lasti : cur])
                    ct += 1
                    dfs(cur + 1,cur, ct)
                    ct -= 1
                    has.remove(s[lasti : cur])
                else:
                    while cur <= len(s) and s[lasti : cur] in has:
                        cur += 1
                    dfs(cur,lasti, ct)
        dfs(1,0,0)
        return self.res
                

