class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr or len(arr) == 1:
            return 0
        
        n = len(arr)
        
        same_val = {}
        for i in range(n):
            if arr[i] not in same_val:
                same_val[arr[i]] = [i]
            else:
                same_val[arr[i]].append(i)
                
        visited = [False] * n
        step = 0
        curr = [0]
        
        while curr:
            next = []
            
            for i in curr:
                if i == n-1: # reached end
                    return step
                
                visited[i] = True
                
                for next_idx in same_val[arr[i]]:
                    if not visited[next_idx]:
                        next.append(next_idx)
                        
                same_val[arr[i]].clear() # critical step: clear the same_val list to prevent redundant search!
                
                for next_idx in [i-1, i+1]:
                    if 0 <= next_idx < n and not visited[next_idx]:
                        next.append(next_idx)
                        
            curr = next
            step += 1
            
        return -1 # unreachable
