n = int(input())
lrr = []
rrr = []
ls = 0
rs = 0
for i in range(n):
    (a, b) = map(int, input().split())
    lrr.append(a)
    rrr.append(b)
    ls += a
    rs += b
mx = abs(ls - rs)
mxi = 0
for i in range(n):
    k = abs(ls - lrr[i] + rrr[i] - (rs - rrr[i] + lrr[i]))
    if mx < k:
        mx = k
        mxi = i + 1
print(mxi)
