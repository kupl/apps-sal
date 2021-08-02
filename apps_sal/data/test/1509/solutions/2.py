import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

s = a[0] * (n - a[0] + 1)
for i in range(1, n):
    if a[i - 1] < a[i]:
        s = s + (a[i] - a[i - 1]) * (n - a[i] + 1)
    if a[i - 1] > a[i]:
        s = s + a[i] * (a[i - 1] - a[i])

print(s)
