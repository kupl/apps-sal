N, M, X = list(map(int, input().split()))
C = []
A = []

for i in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])

ans = -1

for i in range(1, 1 << N):
    price = 0
    skill = [0] * M
    b = len(bin(i)) - 2
    for j in range(b):
        price += C[j] * (i >> j & 1)
        for k in range(M):
            skill[k] += A[j][k] * (i >> j & 1)

    if min(skill) >= X and (price < ans or ans < 0):
        ans = price

print(ans)

