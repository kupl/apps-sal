(n, d) = map(int, input().split())
a = []
for i in range(d):
    a.append(input())
cur = 0
mx = 0
for i in range(d):
    ok = True
    for j in range(n):
        if a[i][j] == '0':
            ok = False
            break
    if not ok:
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 0
print(mx)
