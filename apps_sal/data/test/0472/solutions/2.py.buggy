def f(x):
    s = str(x)
    ans = 0
    for i in s:
        ans += ord(i) - ord('0')
    return ans


n = int(input())
for sx in range(1, 91):
    x = ((sx * sx + 4.0 * n)**0.5 - sx) / 2.0
    if abs(x - round(x)) > 1e-5:
        continue
    lx = int(x)
    if f(lx) != sx:
        continue
    if lx * lx + sx * lx != n:
        continue
    print(lx)
    return
print(-1)
