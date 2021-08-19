
N = int(input())
a = list(map(int, input().split()))
# >0
r = 0
res = 0
for i in range(N):
    sa = 0
    r += a[i]
    if i % 2 == 0:
        if r <= 0:
            sa = 1 - r
            r += sa
    else:
        if r >= 0:
            sa = r + 1
            r -= sa
    res += sa

# <0
r = 0
res2 = 0
for i in range(N):
    sa = 0
    r += a[i]
    if i % 2 == 1:
        if r <= 0:
            sa = 1 - r
            r += sa
    else:
        if r >= 0:
            sa = r + 1
            r -= sa
    res2 += sa
print((min(res, res2)))
