class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        res = 0
        v = A[0]
        max_sofar = v
        for i in range(len(A)):
            max_sofar = max(max_sofar, A[i])
            if A[i] < v:
                v = max_sofar
                res = i
                
        return res+1
