class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        running = [0]
        for num in A:
            running.append(running[-1] + num)

        result = math.inf
        deque = collections.deque([0])
        r = 1

        while r < len(running):
            if not deque:
                deque.append(r)
                r += 1
                continue

            while deque and r < len(running) and running[r] - running[deque[0]] < K:

                while deque and running[r] <= running[deque[-1]]:
                    deque.pop()

                deque.append(r)
                r += 1

            if r == len(running):
                break

            while deque and running[r] - running[deque[0]] >= K:
                l = deque.popleft()
                result = min(result, r - l)

        return result if result != math.inf else -1

        '''
        
                while deque and running[r] <= running[deque[-1]]: 
                    deque.pop()
                    
                    
        l = 0
        r = 1 
        
        while r < len(running): 
            
            while r < len(running) and running[r] - running[l] < K: 
                r += 1 
            while l < r and running[r] - running[l+1] >= K: 
                l += 1
            result = min(result, r-l)
            r += 1
            l  += 1
            
        return result
            
        
            while r < len(running): 
            while deque and running[r] - running[deque[0]] >= K:
                result = min(result, i-deque[0])
                deque.popleft()
            while deque and running[r] <= running[deque[-1]]:
                deque.pop()
            deque.append(r)
            
        return result if result != math.inf else -1
    
    
                
            while r < len(running)-1 and running[r] - running[l] < s: 
                r += 1 

            while l < r and running[r] - running[l] >= s:
                result = min(result, r-l)                
                l += 1
                
            r += 1
        '''
