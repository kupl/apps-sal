class Solution:
    def minOperations(self, target: List[int]) -> int:
        # Initialize result (Count of minimum moves)  
        result = 0;  
        n = len(target)

        # Keep looping while all elements of  
        # target don't become 0.  
        while (True):  

            # To store count of zeroes in  
            # current target array  
            zero_count = 0;  

            # To find first odd element  
            i = 0;  
            while (i < n): 

                # If odd number found  
                if ((target[i] & 1) > 0):  
                    break;  

                # If 0, then increment  
                # zero_count  
                elif (target[i] == 0):  
                    zero_count += 1; 
                i += 1; 

            # All numbers are 0  
            if (zero_count == n):  
                return result;  

            # All numbers are even  
            if (i == n):  

                # Divide the whole array by 2  
                # and increment result  
                for j in range(n): 
                    target[j] = target[j] // 2;  
                result += 1;  

            # Make all odd numbers even by  
            # subtracting one and increment result.  
            for j in range(i, n):  
                if (target[j] & 1):  
                    target[j] -= 1;  
                    result += 1;  
    
                    
                    
        
            
            
            
    

