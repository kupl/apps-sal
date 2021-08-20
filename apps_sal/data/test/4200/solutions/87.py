(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
total = sum(a)
cnt = 0
for _a in a:
    if _a * 4 * m >= total:
        cnt += 1
if cnt >= m:
    print('Yes')
else:
    print('No')
