n = int(input())
a = list(map(int, input().split()))
m = 0
t = 0
for i in range(n):
    m += a[i]
for i in range(n):
    t += 2 * a[i] >= m
if t == 0:
    print('Yes')
else:
    print('No')
