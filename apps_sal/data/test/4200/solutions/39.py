n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

std = sum(a) * (1 / (4 * m))

cnt = 0
for i in range(n):
    if a[i] >= std:
        cnt += 1

if cnt >= m:
    print('Yes')
else:
    print('No')
