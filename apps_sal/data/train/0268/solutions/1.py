class Solution:
    def baseNeg2(self, N):
        res = []
        while N != 0:
            m = N %(-2)
            if m == -1:
                m = 1
            N = (N-m) // (-2)
            res.append(str(m))
            
        return ''.join(res[::-1]) or '0'
