class Solution:
    def maxSatisfied(self, A: List[int], G: List[int], X: int) -> int:
        res = 0
        s = 0
        ws = 0
        left = []
        for i in range(len(A)):
            c, g = A[i], G[i]
            s += (1-g)*c
            ws += g*c
            if i>=X:
                ws -= A[i-X] * G[i-X]
            res = max(res, ws)
            # print(i,j,s,res)
        return res+s
