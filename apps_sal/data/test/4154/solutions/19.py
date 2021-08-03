N, M = map(int, input().split())
L = []
R = []
ans = 0
for j in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
Lmax = max(L)
Rmin = min(R)
for i in range(N):
    if Lmax <= i + 1 and i + 1 <= Rmin:
        ans += 1
print(ans)
