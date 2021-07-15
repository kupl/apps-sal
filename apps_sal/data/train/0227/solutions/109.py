class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
            start, end = 0,0
            max_len = 0
            numzeros = 0
            while end < len(A):
                if A[end] == 0:
                    numzeros += 1
                while numzeros > K:
                    # shrink window
                    if A[start] == 0:
                        numzeros -= 1
                    start += 1
                max_len = max(max_len, end-start+1)
                end += 1
            return max_len
                

