class Solution:
    def knightDialer(self, n: int) -> int:
        if not n:
            return 0
        if n == 1:
            return 10
        
        steps = [1] * 10
        
        mapping = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5:[], 6:[1,7, 0], 7:[2, 6], 8:[1,3], 9:[2,4], 0:[4,6]}
        
        for i in range(2, n+1):
            newSteps = [0] * 10
            for i in range(10):
                for j in mapping[i]:
                    newSteps[i] += steps[j]
                    newSteps[i] %= 10**9 + 7
                    
                    
            steps = newSteps
            
        return sum(steps) % (10**9 + 7)            
