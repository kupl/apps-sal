class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def dfs(start, count):
            if start < 0 or start >=len(arr):
                return False
            if count >= len(arr):
                return False
            if not arr[start]:
                return True
            return dfs(arr[start]+start, count+1) or dfs(start-arr[start], count+1)
        return dfs(start, 0)
