(n, m) = map(int, input().split())
aa = list(map(int, input().split()))
total_aa = sum(aa)
cnt = 0
for a in aa:
    if a >= sum(aa) / (4 * m):
        cnt += 1
if cnt >= m:
    print('Yes')
else:
    print('No')
