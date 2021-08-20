n = int(input())
L = []
ans = 0
for i in range(n):
    a = int(input())
    for j in range(a):
        (x, y) = list(map(int, input().split()))
        L.append((i, x - 1, y))
for i in range(1 << n):
    flg = True
    for (j, x, y) in L:
        if i >> j & 1 and i >> x & 1 != y:
            flg = False
            break
    if flg:
        ans = max(ans, sum((i >> j & 1 for j in range(n))))
print(ans)
