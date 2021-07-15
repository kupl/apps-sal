n, m  = list(map(int, input().split()))

po = []
ps = []
diffs = []

for i in range(n):
    a, b =  list(map(int, input().split()))
    po.append(a)
    ps.append(b)
    diffs.append(a-b)
tlen  = sum(po)
tslen = sum(ps)

diffs.sort(reverse = True)

if sum(po) <= m:
    print(0)
    return
if sum(ps) > m:
    print(-1)
    return

r = sum(po)
cnt = 0
for d in diffs:
    cnt += 1
    r -= d
    if r<=m:
        print(cnt)
        return




