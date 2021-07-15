class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {x:i for i, x in enumerate(A)}
        m = collections.defaultdict(lambda:2)
        res = 0
        for i2 in range(2, len(A)):
            for i0 in range(i2):
                x1 = A[i2] - A[i0]
                if x1 <= A[i0]:
                    break
                if x1 in index:
                    i1 = index[x1]
                    m[(i1, i2)] = m[(i0, i1)] + 1
                    res = max(res, m[(i1, i2)])
        return res
        

                    

        

