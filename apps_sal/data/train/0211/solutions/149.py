from collections import Counter


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 0

        def check(C):
            for char in list(C.keys()):
                if C[char] > 1:
                    return False
            return True

        curr = []

        def dfs(i):
            nonlocal ans
            if i == n:
                C = Counter(curr)
                if (check(C)):
                    ans = max(ans, len(list(C.keys())))
                return
            for j in range(i, n):
                curr.append(s[i:j + 1])
                dfs(j + 1)
                curr.pop()
        dfs(0)
        return ans
