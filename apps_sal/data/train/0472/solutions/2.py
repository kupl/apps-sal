import sys
sys.setrecursionlimit(10**6) 

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:  
        return self.canReach2(arr, start, [])
        
    def canReach2(self, arr, start, visited):
        if start >= len(arr) or start < 0 or start in visited:
            return False
        if arr[start] == 0:
            return True

        visited.append(start)
        # print(start)
        res = self.canReach2(arr, start + arr[start], visited) or self.canReach2(arr, start - arr[start], visited)
        if res is False:
            visited.pop()
        return res
