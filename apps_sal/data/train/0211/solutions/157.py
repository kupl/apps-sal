class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(index, visited):
            nonlocal ans

            if s[index:n] and s[index:n] not in visited:
                ans = max(ans, len(visited) + 1)

            for i in range(index, n):
                if s[index:i] and s[index:i] not in visited and len(visited) + 1 + n - i > ans:
                    visited.add(s[index:i])
                    dfs(i, visited)
                    visited.remove(s[index:i])

        n, ans = len(s), 0
        dfs(0, set())
        return ans
