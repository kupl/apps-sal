class Solution:
    count = 0

    def dfs(self, arr, i, visited):
        for index in range(i + 1, len(arr)):
            visit = True
            for j in range(0, len(arr[index])):
                if arr[index][j] in visited:
                    for k in range(0, j):
                        visited.remove(arr[index][k])
                    visit = False
                    break
                else:
                    visited.add(arr[index][j])
            if visit:
                self.count = max(self.count, len(visited))
            self.dfs(arr, index, visited)
            for char in arr[index]:
                if char in visited and visit:
                    visited.remove(char)

    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 0:
            return 0
        visited = set()
        self.count = 0
        self.dfs(arr, -1, visited)
        return self.count
