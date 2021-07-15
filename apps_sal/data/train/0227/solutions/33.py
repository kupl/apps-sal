class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        longest = start = end = zeroes = 0
        while end < len(A):
            num = A[end]

            if not num:
                zeroes += 1
            end += 1
            while zeroes > K:
                if A[start] == 0:
                    zeroes -= 1
                start += 1
            longest = max(longest, end - start)
        return longest 

