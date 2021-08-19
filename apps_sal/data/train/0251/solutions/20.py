class Solution:

    def clumsy(self, N: int) -> int:
        A = []
        for i in range(N):
            A.append(str(N - i))
            if i % 4 == 0:
                A.append('*')
            elif i % 4 == 1:
                A.append('//')
            elif i % 4 == 2:
                A.append('+')
            else:
                A.append('-')
        A.pop()
        return eval(''.join(A))
