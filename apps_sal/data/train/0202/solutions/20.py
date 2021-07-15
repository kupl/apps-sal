class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        up = [1]*N
        for i in range(1, N):
            if A[i]>A[i-1]: up[i]+=up[i-1]
        down = [1]*N
        for i in range(N-2,-1, -1):
            if A[i]>A[i+1]: down[i]+=down[i+1]
        # print(up, down)
        return max([u+d-1 for u, d in zip(up, down) if u>1 and d>1 and u+d-1>=3] or [0])
