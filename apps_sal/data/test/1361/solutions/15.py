import sys
nu = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
r = max(a)
for j in range(1, nu - 1):
    x = 0
    b = a[:]
    b.remove(a[j])
    for i in range(0, nu - 2):
        x = max(x, b[i + 1] - b[i])
    r = min(r, x)
print(r)
