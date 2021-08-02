a, b, x = list(map(int, input().split()))
mn = "0"
mncnt = a
mx = "1"
mxcnt = b
res = ""
if a > b:
    mn, mx = mx, mn
    mncnt = b
    mxcnt = a
if x % 2 == 0:
    res += (mx + mn) * (x // 2)
    res += mn * (mncnt - x // 2)
    res += mx * (mxcnt - x // 2)
else:
    res += (mx + mn) * (x // 2)
    res += mx * (mxcnt - (x // 2))
    res += mn * (mncnt - (x // 2))
print(res)
