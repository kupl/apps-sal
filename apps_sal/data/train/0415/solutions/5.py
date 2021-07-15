class Solution:
    def minSwap(self, A, B):
        N = len(A)
        #keep, swap = [0] * N, [0] * N
        #keep, swap = [N] * N, [N] * N
        keep, swap = [_ for _ in range(N)], [_ for _ in range(N)]
        swap[0] = 1                                      # important!
        for i in range(1, N):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]                      # keep, keep
                swap[i] = swap[i-1] + 1                  # swap, swap
            if A[i] > B[i-1] and B[i] > A[i-1]:
                swap[i] = min(swap[i], keep[i-1] + 1)    # keep, swap
                keep[i] = min(keep[i], swap[i-1])        # swap, keep
        return min(keep[-1], swap[-1])
    
class Solution:
    def minSwap(self, A, B):
        N = len(A)
        keep, swap = [_ for _ in range(N)], [_ for _ in range(N)]
        swap[0] = 1
        for i in range(1, N):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                if keep[i-1] + 1 < swap[i]: swap[i] = keep[i-1] + 1
                if swap[i-1] < keep[i]: keep[i] = swap[i-1]
        return min(keep[-1], swap[-1])
