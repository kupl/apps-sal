class Solution:
    def splitArraySameAverage(self, A):
        N, S = len(A), sum(A)
        if N == 1: return False
        A = [z * N - S for z in A] 
        mid, left, right = N//2, {A[0]}, {A[-1]}


        if not any((S*size) % N == 0 for size in range(1, mid+1)): return False

        for i in range(1, mid): left |= {z + A[i] for z in left} | {A[i]}
        for i in range(mid, N-1): right |= {z + A[i] for z in right} | {A[i]}
        if 0 in (left|right): return True


        left -= {sum(A[:mid])}
        return any(-ha in right for ha in left)
