class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans, n = 0, len(s)

        def dfs(i, cnt, visited):
            nonlocal ans, n
            if i == n:
                ans = max(ans, cnt)
            for j in range(i + 1, n + 1):
                if s[i:j] in visited:
                    continue
                visited.add(s[i:j])
                dfs(j, cnt + 1, visited)
                visited.remove(s[i:j])
        dfs(0, 0, set())
        return ans
