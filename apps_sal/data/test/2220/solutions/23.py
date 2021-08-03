n, m, k = map(int, input().split())
a = list(map(int, input().split()))
mx, mxx = 0, 0
for i in a:
    if i >= mx:
        mxx = mx
        mx = i
    elif i > mxx:
        mxx = i
if k == m:
    print(mx * m)
else:
    x = m // (k + 1)
    ans = x * (mx * k + mxx) + (m - (k + 1) * x) * mx
    print(ans)
