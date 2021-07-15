class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.res = 0
        partition = []
        def backtrack(start_i):
            if start_i == len(s):
                self.res = max(self.res, len(set(partition)))
            else:
                for j in range(start_i + 1, len(s) + 1):
                    partition.append(s[start_i:j])
                    backtrack(j)
                    partition.pop()
        backtrack(0)
        return self.res
