class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            neighbors = []
            if i - 1 >= 0:
                neighbors.append(A[i - 1])
            if i + 1 < len(A):
                neighbors.append(A[i + 1])
            res += min(neighbors) * A.pop(i)
        return res
