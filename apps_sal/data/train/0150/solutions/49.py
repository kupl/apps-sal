class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        mins = [float('inf')]*(n-1)+[A[-1]]
        for i in range(n-2, -1, -1):
            mins[i] = min(A[i], mins[i+1])

        maxi = 0
        for i in range(n-1):
            maxi = max(maxi, A[i])
            if maxi<=mins[i+1]:
                return i+1
        return -1
