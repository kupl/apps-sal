import sys
n, m = map(int, input().split())
a = [[int(i) for i in input().split()] for j in range(n)]
last = 0
for i in range(n):
    if a[i][0] <= last:
        last = max(last, a[i][1])
if last >= m:
    print('YES')
else:
    print('NO')
