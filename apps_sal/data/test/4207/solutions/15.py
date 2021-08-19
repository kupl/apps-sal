from collections import defaultdict


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
x = defaultdict(int)
p = 0
for i in range(n):
    if a[i] == 0 and b[i] == 0:
        p += 1
    elif a[i] != 0:
        if a[i] * b[i] < 0:
            z = 0
        else:
            z = 1
        v = gcd(abs(a[i]), abs(b[i]))
        x[z, abs(a[i]) // v, abs(b[i]) // v] += 1
if len(x) > 0:
    print(max(x.values()) + p)
else:
    print(p)
