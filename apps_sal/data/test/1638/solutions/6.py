n = int(input())
L = list(map(int, input().split()))
ans = [0] * n
sA = 0
for top in range(n):
    r = []

    if top != 0:
        left = []
        now = L[top]
        for i in range(top)[::-1]:
            now = min(now, L[i])
            left.append(now)
        r += left[::-1]
    r.append(L[top])
    if top != n - 1:
        right = []
        now = L[top]
        for i in range(top + 1, n):
            now = min(now, L[i])
            right.append(now)
        r += right
    sr = sum(r)
    if sA < sr:
        sA = sr
        ans = r
for i in range(n):
    print(ans[i], end=' ')
