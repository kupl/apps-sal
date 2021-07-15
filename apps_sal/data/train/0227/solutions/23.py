class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        '''naive
        
        
        sliding window
        keep growing sliding window rhs as num of 0s in window is >k
        when num 0s == k, slide lhs of window until k > num 0s again
        keep track of largest sliding window'''
        
        
        if not A:
            return 0
        
        best_window_len = 0
        p, q = 0, 0
        
        num_zeros = 0
        #if A[q] == 0: num_zeros += 1
        
        while q < len(A):
            if A[q] == 0: num_zeros += 1
            #print(p, q, q - p)
            if num_zeros > K:
                best_window_len = max(q - p, best_window_len)
                #print(\"running best:\", best_window_len)
                while num_zeros > K:
                    if A[p] == 0:
                        num_zeros -= 1
                    p += 1
            q+=1
            
        best_window_len = max(q - p, best_window_len)
        #if p == 0:
            #best_window_len+=1
        #print(best_window_len)
        return best_window_len
                

