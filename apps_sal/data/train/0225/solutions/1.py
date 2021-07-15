class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        d = [0] * n
        
        force = 0
        
        for i in range(n):
            c = dominoes[i]
            
            if c == 'R':
                force = n
            elif c == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
                
            d[i] += force
            
        force = 0
        
        for i in range(n-1, -1, -1):
            c = dominoes[i]
            
            if c == 'R':
                force = 0
            elif c == 'L':
                force = n
            else:
                force = max(force - 1, 0)
                
            d[i] -= force
            
        def inner():
            for f in d:
                if f == 0:
                    yield '.'
                elif f > 0:
                    yield 'R'
                else:
                    yield 'L'
                    
        return ''.join(inner())
