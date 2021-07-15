import collections

class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        ''' Place all values into dicts and start counting from the bottom
        '''
        if not A:
            return True
        
        counter = collections.Counter(A)
        
        for v in sorted(counter, key = abs):
            if counter[2 * v] < counter[v]:
                return False
            counter[2 * v] -= counter[v]
        return True
        
            
                
                    
            
        

