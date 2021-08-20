import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = a[0]
mi = 0
for i in range(n):
    if abs(a[i]) > abs(m):
        m = a[i]
        mi = i
print(2 * n - 1)
for i in range(n):
    print((mi + 1, i + 1))
if m >= 0:
    for i in range(n - 1):
        print((i + 1, i + 2))
else:
    for i in range(n - 1):
        print((n - i, n - 1 - i))
