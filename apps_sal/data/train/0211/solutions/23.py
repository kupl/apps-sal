class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        exist = collections.defaultdict(int)
        self.result = 0
        n = len(s)

        def dfs(index: int) -> None:
            if index == n:
                self.result = max(self.result, len(exist))
                return
            for i in range(index + 1, n + 1):
                st = s[index:i]
                exist[st] += 1
                dfs(i)
                exist[st] -= 1
                if exist[st] == 0:
                    del exist[st]
        dfs(0)
        return self.result
