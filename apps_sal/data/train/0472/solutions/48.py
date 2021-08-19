class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def helper(visited, arr, start):
            if start < 0 or start >= len(arr) or start in visited:
                return False
            visited.add(start)
            if arr[start] == 0:
                return True
            return helper(visited, arr, start - arr[start]) or helper(visited, arr, start + arr[start])
        return helper(visited, arr, start)
