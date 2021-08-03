from sys import stdin, stdout
n, m, k = list(map(int, stdin.readline().split()))
x, s = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
d = list(map(int, stdin.readline().split()))
a.insert(0, x)
b.insert(0, 0)
c.insert(0, 0)
d.insert(0, 0)
ans = 1 << 100
for it in range(m + 1):
    mana = s - b[it]
    if mana < 0:
        continue
    lo, hi = 0, k
    while lo != hi:
        mid = (lo + hi + 1) // 2
        if d[mid] <= mana:
            lo = mid
        else:
            hi = mid - 1
    ans = min(ans, (n - c[lo]) * a[it])
stdout.write(str(ans) + '\n')
