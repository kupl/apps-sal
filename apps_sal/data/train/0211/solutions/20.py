class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.maxsplits = 0

        def DFS(i, substring_set):
            if i == len(s):
                self.maxsplits = max(len(substring_set), self.maxsplits)
                return

            for j in range(i + 1, len(s) + 1):
                DFS(j, substring_set | {s[i: j]})

        DFS(0, set())
        return self.maxsplits
