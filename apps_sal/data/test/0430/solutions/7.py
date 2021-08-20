import sys
f = sys.stdin
n = int(f.readline().strip())
a = [int(u) for u in f.readline().strip().split()]
a = sorted(a, reverse=True)
W1 = 0
W2 = 0
for i in range(int(n / 2)):
    W1 += a[2 * i]
    W2 += a[2 * i + 1]
if n % 2 == 1:
    W2 += a[n - 1]
if W1 == W2:
    res = 'YES'
else:
    res = 'NO'
print(res)
