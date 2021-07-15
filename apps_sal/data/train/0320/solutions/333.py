class Solution:
    def minOperations(self, target: List[int]) -> int:
        result = 0  
        while (True):    
            zero_count = 0
            i = 0
            n = len(target)
            while (i < n): 
                if ((target[i] & 1) > 0):  
                    break;  
                elif (target[i] == 0):  
                    zero_count += 1
                i += 1 
            if (zero_count == n):  
                return result
            if (i == n):  
                for j in range(n): 
                    target[j] = target[j] // 2 
                result += 1 
            for j in range(i, n):  
                if (target[j] & 1):  
                    target[j] -= 1 
                    result += 1

