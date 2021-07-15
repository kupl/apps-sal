import math

t = int(input())

for q in range(t):
    n = int(input())
    L = [int(i) for i in input().split()]
    G = list(sorted(L))
    f = min(L)
    t = True
    for i in range(n):
        if L[i] % f != 0 and G[i] != L[i]:
            t = False
    if t:
        print('YES')
    else:
        print('NO')

