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
    # 如果中间有一个数字变大，我不更新v， v只是之前最大的数
    # [32,57,24,19,0,24,49,67,87,87]  如果我不更新v，32 会一直最大，那么49 就归在右边了

