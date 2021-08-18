n, m = list(map(int, input().split()))
arr = [0] * (n + 1)
for i in range(n):
    arr[i] = input()
cntb = 0
mn = 200
mx = 0
for i in range(n):
    first = True
    for j in range(m):
        if arr[i][j] == 'B':
            cntb += 1
            if first:
                mn = min(mn, j)
                mx = max(mx, j)
                first = False
            else:
                mx = max(mx, j)
mn2 = 200
mx2 = 0
if cntb == 0:
    print(1)
    return
elif cntb == 1:
    print(0)
    return
for i in range(m):
    first = True
    for j in range(n):
        if arr[j][i] == 'B':
            if first:
                mn2 = min(mn2, j)
                mx2 = max(mx2, j)
                first = False
            else:
                mx2 = max(mx2, j)
val = max(mx - mn + 1, mx2 - mn2 + 1)
if val > m or val > n:
    print(-1)
    return
print(val * val - cntb)
