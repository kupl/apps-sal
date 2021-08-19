class Solution:

    def numTeams(self, A) -> int:
        L = len(A)
        result = 0
        for j in range(1, L - 1):
            (x, loL, loR, hiL, hiR) = (A[j], 0, 0, 0, 0)
            for i in range(j):
                if A[i] < x:
                    print('x', x)
                    print('A[i]', A[i])
                    loL += 1
                else:
                    hiL += 1
            for k in range(j + 1, L):
                if A[k] < x:
                    loR += 1
                else:
                    hiR += 1
            result += loL * hiR + hiL * loR
            print('resut', result)
        return result
