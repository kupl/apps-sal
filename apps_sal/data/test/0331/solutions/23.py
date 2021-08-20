(n, m, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
m = m - 1
lp = m - 1
rp = m + 1
found = False
ansr = 10000000
if rp < n:
    while not found and rp < n:
        if l[rp] != 0 and l[rp] <= k:
            ansr = rp - m
            found = True
        rp += 1
    found = False
else:
    ansr = 100000
ansl = 1000000
if lp >= 0:
    while not found and lp >= 0:
        if l[lp] != 0 and l[lp] <= k:
            ansl = m - lp
            found = True
        lp -= 1
else:
    ansl = 100000
print(min(ansr, ansl) * 10)
