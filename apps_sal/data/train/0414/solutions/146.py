from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        queue = deque()
        
        for x in arr:
            queue.append(x)
            
        
        curr = queue.popleft()
        
        curr_count = 0
        
        while curr_count < k and curr_count < len(arr):
            temp = queue.popleft()
            
            if curr > temp:
                curr_count += 1
                queue.append(temp)
            else:
                curr_count = 1
                queue.append(curr)
                curr = temp
                
                
            print(curr_count)
                
        return curr
