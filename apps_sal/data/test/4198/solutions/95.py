(A, B, X) = map(int, input().split())
L = 0
R = 1000000000
while R - L > 1:
    M = (L + R) // 2
    P = A * M + B * len(str(M))
    if P <= X:
        L = M
    else:
        R = M - 1
if R == L:
    print(L)
elif A * R + B * len(str(R)) <= X:
    print(R)
else:
    print(L)
