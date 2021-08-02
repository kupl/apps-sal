import sys

n, m = [int(w) for w in input().split()]
x = [int(w) for w in input().split()]
t = [int(w) for w in input().split()]

if m == 1:
    print(n)
    return

p = []
tx = []
for i in range(n + m):
    (tx if t[i] == 1 else p).append(x[i])

a = [0] * m
i = 0
for pi in p:
    while i < m - 1 and pi > (tx[i] + tx[i + 1]) / 2:
        i += 1
    a[i] += 1

print(" ".join(str(ai) for ai in a))
