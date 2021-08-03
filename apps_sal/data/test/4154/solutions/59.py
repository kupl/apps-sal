n, m = map(int, input().split())
L = []
R = []
for _ in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
ans = min(R) - max(L) + 1
print(ans) if ans > 0 else print(0)
