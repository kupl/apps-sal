N, M = map(int, input().split())
L, R = [], []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

m = max(L)
M = min(R)
if M >= m:
    print(M - m + 1)
else:
    print(0)
