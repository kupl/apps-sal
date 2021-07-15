class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # imagine blank spaces equal to 
        # the number of rolls
        
        # _ _ _ _ 
        
        # every time we roll, it could be any of 1-6 numbers
        
        # so imagine the first number is 1
        # what are possibilities for the rest
        # the rest can again be
        
        # what do we want function to return.
        # instead of returning, can just increment count when reaching the end
        
        cache = {}
        
        def sim(n, count, curr_element):    
            if curr_element:
                if count > rollMax[curr_element-1]:
                    return float('inf')
                
            if (n,count,curr_element) in cache:
                return cache[(n,count,curr_element)]
            
            if n==0:
                return 1

            # basically how many ways can I reach end from current point
            all_ans = 0
            for i in range(1,7):
                if curr_element == i:
                    ans = sim(n-1, count+1, i)
                else:
                    ans = sim(n-1, 1, i)
                    
                if ans!=float('inf'):
                    all_ans += ans 
                    
            cache[(n,count, curr_element)] = all_ans
            return all_ans
                
        
        return sim(n, 0, 0) % 1000000007
