n = int(input())
plist = list(map(int, input().split()))
nlist = sorted(plist)

ng_cnt = 0
for p, n in zip(plist, nlist):
    if p != n:
        ng_cnt += 1
if ng_cnt >2:
    print('NO')
else:
    print('YES')
