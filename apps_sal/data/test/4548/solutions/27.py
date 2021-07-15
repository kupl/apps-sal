N, M, X = map(int,input().split())
A = map(int,input().split())

L = 0
R = 0

for ai in A:
    if ai < X:
        L = L + 1
    else:
        R = R + 1
print(min(L, R))
