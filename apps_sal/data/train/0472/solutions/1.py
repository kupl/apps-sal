class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 not in arr:
            return False
        visited = set()
        queue = []
        queue.append(start)
        visited.add(start)
        while len(queue):
            curr_index = queue.pop()
            if arr[curr_index] == 0:
                return True
            next_index = curr_index + arr[curr_index]
            if next_index < len(arr) and next_index not in visited:
                visited.add(next_index)
                queue.append(next_index)
            next_index = curr_index - arr[curr_index]
            if next_index >= 0 and next_index not in visited:
                visited.add(next_index)
                queue.append(next_index)
        return False
                
            
        
        

