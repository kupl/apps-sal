class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        dq = collections.deque([start])
        visited = set([start])
        
        while dq:
            
            curr = dq.pop()
            
            if arr[curr] == 0:
                return True
            
            if (curr + arr[curr]) not in visited and (curr + arr[curr]) < len(arr):
                dq.appendleft(curr + arr[curr])
                visited.add(curr + arr[curr])
            if (curr - arr[curr]) not in visited and (curr - arr[curr]) >= 0:
                dq.appendleft(curr - arr[curr])
                visited.add(curr - arr[curr])
        
        return False
