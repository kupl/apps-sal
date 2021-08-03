import sys


n = int(next(sys.stdin))

line = next(sys.stdin).strip()
a = list(map(int, line.split()))
b = list(map(int, line.split()))

ab = set(a).union(set(b))
p = 0
for i in range(n):
    for j in range(i + 1, n):
        x = a[i] ^ b[i]
        if x in ab:
            p += 1

if p % 2 == 0:
    print("Karen")
else:
    print("Koyomi")
