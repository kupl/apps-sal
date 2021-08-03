class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)

        hint = [0] * N  # Keeps track of first index after a flip

        counter = 0  # Total flips

        flip = 0  # Whether we are looking at a flipped array or not

        for i, x in enumerate(A):
            # If hint[i] == 1, then the flip whose last index was i-1 must be removed from our flip counter
            flip = (flip + hint[i]) % 2

        # If x is 1 and flipped or x is 0 and unflipped, then it is 0, so we need to flip the bit.
            if (x == 1 and flip == 1) or (x == 0 and flip == 0):
                counter += 1  # Add to the flip counter

                # Check if K-bit flip goes past end of array.
                if i + K > N:
                    return -1

                # We flipped, so we change our flip value for the next iteration of the loop
                flip = 1 - flip

                # Keep track of first index after flip
                if i + K < N:
                    hint[i + K] = 1

        return counter
