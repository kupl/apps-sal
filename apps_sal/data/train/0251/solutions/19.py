class Solution:
    def clumsy(self, N: int) -> int:
        res = []
        
        counter = 0
        for num in reversed(list(range(1, N + 1))):
            res.append(str(num))
            if counter == 0:
                res.append('*')
            elif counter == 1:
                res.append('//')
            elif counter == 2:
                res.append('+')
            elif counter == 3:
                res.append('-')
            
            counter += 1
            if counter == 4:
                counter = 0
            
        res.pop()
        
        return eval(''.join(res))

