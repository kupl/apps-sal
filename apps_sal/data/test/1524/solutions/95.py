li = list(input())
n = len(li)
ans = [0 for _ in range(n)]
rcnt = 0
lcnt = 0
ridx = 0
lidx = 0
for i in range(1, n):
    if li[i - 1] == 'R':
        rcnt += 1
        if li[i] == 'L':
            ridx = i - 1
            lidx = i
            if i == n - 1:
                lcnt += 1
                ans[ridx] = (rcnt + 1) // 2 + lcnt // 2
                ans[lidx] = (lcnt + 1) // 2 + rcnt // 2
                rcnt = 0
                lcnt = 0
    if li[i - 1] == 'L':
        lcnt += 1
        if li[i] == 'R' or i == n - 1:
            if i == n - 1:
                lcnt += 1
            ans[ridx] = (rcnt + 1) // 2 + lcnt // 2
            ans[lidx] = (lcnt + 1) // 2 + rcnt // 2
            rcnt = 0
            lcnt = 0
print(*ans)
