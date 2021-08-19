class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        curr_k = 0
        pointer_start = 0
        pointer_end = 0
        max_ones = 0
        curr_ones = 0
        while pointer_end < len(A):
            if A[pointer_end] == 0:
                if curr_k >= K:
                    if A[pointer_start] == 0:
                        curr_k -= 1
                    pointer_start += 1
                    curr_ones -= 1
                else:
                    pointer_end += 1
                    curr_ones += 1
                    curr_k += 1
            else:
                pointer_end += 1
                curr_ones += 1
            max_ones = max(curr_ones, max_ones)
        return max_ones
