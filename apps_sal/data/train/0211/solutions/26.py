class Solution:
    def _dfs(self, s, i, visited):
        if i == len(s):
            yield len(visited)
            return
        
        for j in range(i + 1, len(s) + 1):
            if s[i:j] not in visited:
                visited.add(s[i:j])
                yield from self._dfs(s, j, visited)
                visited.remove(s[i:j])
        
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        
        return max(self._dfs(s, 0, set()))
