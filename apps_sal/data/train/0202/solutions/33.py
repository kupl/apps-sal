class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res = 0
        i = 0
        
        while i < len(A):
            j = i
            while j + 1 < len(A) and A[j] < A[j+1]:
                j += 1
            mid = j
            while j + 1 < len(A) and A[j] > A[j+1]:
                j += 1
            if i < mid < j:
                res = max(res, j-i+1)
            if i == j:
                i +=1
            else:
                i = j
        
        return res
