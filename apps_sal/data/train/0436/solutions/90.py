class Solution:
    def minDays(self, n: int) -> int:
        
        from collections import deque
        q = deque()
        q.append((n, 0))
        visited = set()
        while q:
            
            new_n, days = q.pop()
            if new_n == 0:
                return days

            if new_n in visited:
                continue
                
            q.appendleft((new_n - 1, days + 1))
            if new_n % 2 == 0:
                q.appendleft((new_n // 2, days + 1))
            if new_n % 3 == 0:
                q.appendleft((new_n // 3, days + 1))           
            
            visited.add(new_n)
        
        return -1
        
    def find(self, n, memo):
        # DFS
        if n <= 1:
            return n
        
        if n in memo:
            return memo[n]
        
        min_val = self.find(n-1, memo)
        
        if n % 2 == 0:
            min_val = min(min_val, self.find(n // 2, memo))
        
        if n % 3 == 0:
            min_val = min(min_val, self.find((n // 3), memo))
        
        memo[n] = min_val + 1
        return memo[n]
        

