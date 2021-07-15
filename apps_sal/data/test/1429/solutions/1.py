n,s = input().split()
n = int(n)

cnt = {}
at = 0
gc = 0
ans = 0
cnt[(0,0)] = 1

for si in s:
    if si == "A":
        at += 1
    elif si=="T":
        at -= 1
    elif si=="G":
        gc += 1
    else:
        gc -= 1
    if (at,gc) in cnt:
        ans += cnt[(at,gc)]
        cnt[(at,gc)] += 1
    else:
        cnt[(at,gc)] = 1
print(ans)
