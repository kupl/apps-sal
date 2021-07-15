class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        start, end, max_length, num_0 = 0, 0, 0, int(not A[0])
        while end < len(A) - 1:
            if num_0 > K:
                if A[start] == 0:
                    num_0 -= 1
                start += 1
            end += 1
            if A[end] == 0:
                num_0 += 1
            if num_0 <= K:
                max_length = end - start + 1
        return max_length
