import sys
Q = int(sys.stdin.readline().strip())
for q in range(0, Q):
    (n, s) = sys.stdin.readline().strip().split()
    n = int(n)
    U = [1]
    D = [1]
    for i in range(0, n - 1):
        if s[i] == '<':
            U[-1] = U[-1] + 1
            D.append(1)
        else:
            D[-1] = D[-1] + 1
            U.append(1)
    m = n
    i = 0
    A = []
    while m > 0:
        for j in range(0, U[i]):
            A.append(str(m - U[i] + j + 1))
        m = m - U[i]
        i = i + 1
    print(' '.join(A))
    m = 0
    i = 0
    A = []
    while i < len(D):
        for j in range(0, D[i]):
            A.append(str(m + D[i] - j))
        m = m + D[i]
        i = i + 1
    print(' '.join(A))
