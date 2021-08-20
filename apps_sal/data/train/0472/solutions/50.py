class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr):
            return self.dfs(arr, start, set())
        return False

    def dfs(self, arr, start, visited):
        if arr[start] == 0:
            return True
        visited.add(start)
        if 0 <= start + arr[start] < len(arr) and start + arr[start] not in visited:
            if self.dfs(arr, start + arr[start], visited):
                return True
        if 0 <= start - arr[start] < len(arr) and start - arr[start] not in visited:
            if self.dfs(arr, start - arr[start], visited):
                return True
        return False
