class Solution:
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        N = len(A)
        if N == 1: return 0
        
        # Find left_end and right start
        left_end, right_start = 0, N - 1
        for i in range(1, N):
            if A[i] >= A[i-1]:
                left_end = i
            else:
                break
        
        for i in range(N-2, -1, -1):
            if A[i] <= A[i+1]:
                right_start = i
            else:
                break
                
        # Increasing array, no need to do anything
        print((left_end, right_start))
        if left_end > right_start: return 0
        ret = min(N - left_end - 1, right_start)
        
        # Two pointer
        j = right_start
        for i in range(left_end + 1):
            if j < N and A[i] <= A[j]:
                ret = min(ret, j - i - 1)
            else:
                while j < N and A[j] < A[i]:
                    j += 1
                ret = min(ret, j - i - 1)
        
        return ret

