N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
imos = [0] * (2 * M + 1)
imos2 = [0] * (2 * M + 1)
res = 0
for i in range(N - 1):
    a, b = A[i] - 1, A[i + 1] - 1
    if a > b:
        b += M
    res += b - a
    if a + 2 >= b + 1:
        continue
    imos[a + 2] += 1
    imos[b + 1] -= 1
    imos2[b + 1] -= (b - a - 1)
P = [0]
l = 0
for k, s in zip(imos, imos2):
    l += k
    P.append(P[-1] + l + s)
Q = P[1:-1]
R = [x + y for x, y in zip(Q[:M], Q[M:])]
print((res - max(R)))
