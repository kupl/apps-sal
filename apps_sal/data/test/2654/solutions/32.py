import numpy as np
N = int(input())
A = []
B = []
for i in range(N):
    (a, b) = [int(x) for x in input().split()]
    A.append(a)
    B.append(b)
C = np.array(A)
D = np.array(B)
m_inf = np.median(C)
m_sup = np.median(D)
if N % 2 == 0:
    ans = 2 * m_sup - 2 * m_inf + 1
else:
    ans = m_sup - m_inf + 1
print(int(ans))
