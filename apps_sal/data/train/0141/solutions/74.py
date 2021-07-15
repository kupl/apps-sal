class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        q = collections.deque(sorted(people))
        
        ans = 0
        
        while len(q) > 1:
            i,x = q.pop(), q[0]
            if i+x <= limit:
                q.popleft()
            ans += 1
        
        return ans + (1 if q else 0)
            
        

