class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        more = {}
        less = {}
        stack = []
        
        B = sorted(range(n), key=lambda i: A[i])
        for i in B:
            while stack and stack[-1] < i:
                more[stack.pop()] = i
                
            stack.append(i)
            
        B = sorted(range(n), key=lambda i: -A[i])
        for i in B:
            while stack and stack[-1] < i:
                less[stack.pop()] = i
                
            stack.append(i)
            
        count = 0
        for i in range(n):
            jumps = 1
            j = i
            while j < n - 1:
                if jumps % 2:
                    j = more[j] if j in more else None
                else:
                    j = less[j] if j in less else None
                    
                if j is None:
                    break
                
                jumps += 1
                    
            if j is not None:
                count += 1
                
        return count
