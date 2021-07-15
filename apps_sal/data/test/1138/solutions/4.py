import sys, math
a = input()
n = len(a)
if n % 2 == 1:
    print(-1)
else:
    U = a.count('U')
    D = a.count('D')
    L = a.count('L')
    R = a.count('R')
    print(int(math.fabs(U - D) + math.fabs(L - R)) // 2)
