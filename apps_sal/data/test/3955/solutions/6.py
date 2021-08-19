import sys
(n, k, x) = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]
tl = 0
l = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    tl |= a[i]
    l[i] = tl
ans = 0
tr = 0
for i in range(0, n):
    ta = tr | a[i] * x ** k | l[i + 1]
    ans = ans if ans > ta else ta
    tr |= a[i]
print(ans)
