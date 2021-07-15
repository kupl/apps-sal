class Solution:
    def minDays(self, n: int) -> int:
        
        if n == 0:
            return 0
        
        current = set([n])
        level = 0
        
        while True:

            level += 1
            temp = set()
            
            for num in current:
                
                if num == 1:
                    return level
                
                if num % 2 == 0:
                    temp.add(num//2)
                if num % 3 == 0:
                    temp.add(num//3)
                temp.add(num-1)
                
            current = temp

