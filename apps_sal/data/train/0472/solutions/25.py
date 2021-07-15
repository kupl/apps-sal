class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        def dfs(index:int)->bool:
            if index < 0 or index >= n:
                return False
            if visited[index]:
                return False
            if arr[index] == 0:
                return True
            visited[index] = True
            left = index - arr[index]
            if dfs(left):
                return True
            right = index + arr[index]
            return dfs(right)
        return dfs(start)
        return ans

