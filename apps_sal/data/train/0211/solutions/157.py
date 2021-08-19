class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # dfs O(2^n) / O(n)
        def dfs(index, visited):
            nonlocal ans

            # if we have not seen the rest, then our answer is at least 1 larger
            if s[index:n] and s[index:n] not in visited:
                ans = max(ans, len(visited) + 1)

            # try each section of the remaining
            for i in range(index, n):
                # only if it doesn't exist yet, and it is not impossible to beat current max
                if s[index:i] and s[index:i] not in visited and len(visited) + 1 + n - i > ans:  # prune
                    visited.add(s[index:i])
                    dfs(i, visited)
                    visited.remove(s[index:i])

        n, ans = len(s), 0
        dfs(0, set())
        return ans
