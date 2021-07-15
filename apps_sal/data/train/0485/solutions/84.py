class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        
        flip_ind = [0] * N # Keeps track of first index after a flip
        
        counter = 0 # Total flips
        
        flip = 0 # Flip counter. The flip counter only matters modulo 2.
        
        for i, x in enumerate(A):
            # If flip_ind[i] == 1, then the flip whose last index was i-1 must be removed from our flip counter
            flip = (flip + flip_ind[i]) % 2
        
            # If x is 1 and flipped or x is 0 and unflipped, then it is 0, so we need to flip the bit.
            if (x == 1 and flip == 1) or (x == 0 and flip == 0):
                counter += 1  # Add to the flip counter
                
                # Check if K-bit flip goes past end of array.
                if i+K > N:
                    return -1
                
                # We flipped, so we change our flip value for the next iteration of the loop
                flip = 1-flip
                
                # Keep track of first index after flip
                if i+K < N:
                    flip_ind[i + K] = 1

        return counter
                

