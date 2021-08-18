n, m, l = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]

anss = []
ans = 0
on = False
for i in range(n):
    if a[i] > l and not on:
        ans += 1
        on = True
    elif a[i] <= l and on:
        on = False

for i in range(m):
    r = [int(s) for s in input().split()]
    if r[0] == 0:
        anss.append(ans)
    else:
        p, d = r[1] - 1, r[2]
        if a[p] <= l and a[p] + d > l:
            add = 1
            if p > 0 and a[p - 1] > l:
                add -= 1
            if p < n - 1 and a[p + 1] > l:
                add -= 1
            ans += add
        a[p] += d

print(*anss, sep='\n')
