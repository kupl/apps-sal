n, l, r = list(map(int, input().split()))
A = [int(i) for i in input().split()]
Cord = [int(i) for i in input().split()]
Cinv = [0 for _ in range(n)]
for i in range(n):
    Cinv[Cord[i] - 1] = i

pmin = -10**18
B = [0 for _ in range(n)]
ans = True
for i in range(n):
    ad = max(l, pmin + A[Cinv[i]] + 1)
    B[Cinv[i]] = ad
    pmin = B[Cinv[i]] - A[Cinv[i]]
    if ad > r:
        ans = False

if ans:
    print(*B)
else:
    print(-1)
