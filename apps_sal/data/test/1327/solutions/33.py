N, M = list(map(int, input().split()))

# 全＋、全ー、
L = []
for i in range(N):
    x, y, z = list(map(int, input().split()))
    a1 = x + y + z
    a2 = -x + y + z
    a3 = -x - y + z
    a4 = -x - y - z
    a5 = x - y + z
    a6 = x - y - z
    a7 = x + y - z
    a8 = -x + y - z
    L.append([x, y, z, a1, a2, a3, a4, a5, a6, a7, a8])

ans = 0
for i in range(3, 11):
    L = sorted(L, key=lambda x: x[i], reverse=True)
    sub = 0
    for j in range(M):
        t = L[j]
        sub += t[i]
    ans = max(ans, sub)
print(ans)
