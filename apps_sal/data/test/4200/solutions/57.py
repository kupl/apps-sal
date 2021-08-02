n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0

s = sum(a)

for x in a:
    if x >= s / (4 * m):
        cnt += 1

if cnt >= m:
    print('Yes')
else:
    print('No')
