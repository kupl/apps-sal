(N, M) = [int(n) for n in input().split()]
L = 0
R = N
for m in range(M):
    (l, r) = [int(n) for n in input().split()]
    L = max(L, l)
    R = min(R, r)
print(R - L + 1 if L <= R else 0)
