L = list(map(int, input().split()))
S = sum(L)
N = 4
for i in range(2**4):
    a = 0
    b = S
    for j in range(N):
        if 1 & (i >> j):
            a += L[j]
            b -= L[j]
    if a == b:
        print('Yes')
        return
print('No')
