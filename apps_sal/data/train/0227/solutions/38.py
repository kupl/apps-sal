'''

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6







'''


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        '''
        Sliding window technique
        '''
        # if there's no array
        if not A:
            return 0

        # define a window
        window = 0

        # define start of the window
        start = 0

        # maximum allowed ones
        max_ones = 0

        # iterate over A
        for it, value in enumerate(A):

            # add value to window
            window += value

            # eviction reached?
            # [1,1,1,0,0,0,1,1,1,1,0]
            if it - start + 1 > window + K:
                window -= A[start]
                start += 1

            # figure the maximum ones possible
            max_ones = max(max_ones, window + K)

        return min(max_ones, len(A))
