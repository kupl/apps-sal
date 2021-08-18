
n, m = map(int, input().split())

if n <= m:
    print(n)
    return

tl = m
tr = n
while tr - tl > 1:
    tm = (tl + tr) // 2
    cnt = tm * (tm + 1) // 2 - m * (m + 1) // 2
    cur = n + (tm - m - 1) * m - cnt
    if cur <= 0:
        tr = tm
    else:
        tl = tm
print(tr)
