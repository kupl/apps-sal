class Solution:

    def longestMountain(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
                
        print(down)
        print(up)
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

