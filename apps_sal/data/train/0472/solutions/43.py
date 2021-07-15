class Solution:
    visited = set()
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        return self.backtrack(arr, start, visited)
    
    def backtrack(self, arr, index, visited):
        if index < 0 or index >= len(arr) or arr[index] < 0:
            return False
        if arr[index] == 0:
            return True
        temp = arr[index]
        arr[index] *= -1
        return self.backtrack(arr, index + temp, visited) or self.backtrack(arr, index - temp, visited)
