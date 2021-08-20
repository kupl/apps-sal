import math
n = 100009
A = [0] * n
B = []


def using_sqrt(limit):
    for k in range(2, limit + 1):
        factor = 0
        if k % 2 == 0 and k != 2:
            continue
        for divisor in range(2, math.floor(math.sqrt(k)) + 1):
            if k % divisor == 0:
                factor += 1
        if factor == 0:
            A[k] = 1
            B.append(k)


using_sqrt(n)
C = [0] * n
for i in B:
    if A[i] == 1 and A[(i + 1) // 2] == 1:
        C[i] = 1
D = []
c = 0
for i in C:
    c += i
    D.append(c)
q = int(input())
for _ in range(q):
    (a, b) = map(int, input().split())
    if C[a] == 1:
        print(D[b] - D[a] + 1)
    else:
        print(D[b] - D[a])
