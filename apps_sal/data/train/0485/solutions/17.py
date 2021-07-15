class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        hint = [0] * N # Keeps track of whether there has been at least one flip at given index
        counter = 0 # Total flips
        flip = 0 # Whether we are looking at a flipped array or not (follow code in for loop, e.g. 1011)
        for i, x in enumerate(A):
            # Check if bit is known to be flipped. If it is flipped and we are looking at a flipped bit, then we can simply set flip to 0
            flip = (flip + hint[i]) % 2
        
        # If x is 1 and flipped or x is 0 and unflipped, then it is 0, so we need to flip the bit.
            if (x == 1 and flip == 1) or (x == 0 and flip == 0):
                counter += 1  # Add to the flip counter
                
                # Check if K-bit flip goes past end of array.
                if i+K > N:
                    return -1
                
                # We flipped, so we change our flip value for the next iteration of the loop
                flip = 1-flip
                
                # 
                if i+K < N:
                    hint[i + K] = 1

        return counter
                

