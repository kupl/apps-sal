(A, B, X) = map(int, input().split())
N = 0
dN = len(str(N))
p = A * N + B * dN
for i in range(N, 10 ** 9, 10000000):
    N += 10000000
    dN = len(str(N))
    p = A * N + B * dN
    if p > X:
        N -= 10000000
        break
for j in range(N, 10 ** 9, 10000):
    N += 10000
    dN = len(str(N))
    p = A * N + B * dN
    if p > X:
        N -= 10000
        break
for k in range(N, 10 ** 9):
    N += 1
    dN = len(str(N))
    p = A * N + B * dN
    if p > X:
        N -= 1
        break
if N > 10 ** 9:
    print(10 ** 9)
else:
    print(N)
