n = int(input())

l = list(map(int, input().split()))
ans = [400001 for i in range(n)]
zs = []
for x in range(n):
    if l[x] == 0:
        zs.append(x)
        ans[x] = 0

for i in zs:
    lp = i - 1
    rp = i + 1
    cntL = 1
    cntR = 1
    while lp != -1:

        if ans[lp] <= cntL:
            break
        ans[lp] = cntL
        cntL += 1
        lp -= 1
    while rp != n:
        if ans[rp] <= cntR:
            break
        ans[rp] = cntR
        cntR += 1
        rp += 1

print(' '.join([str(x) for x in ans]))
