from math import gcd


n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

d = {}
w = 0
for i in range(n):
    if a[i] != 0:
        c = gcd(abs(a[i]), abs(b[i]))
        z = 1
        if a[i] * b[i] < 0:
            z = -1
        d[(abs(b[i]) // c, abs(a[i]) // c, z)] = d.get((abs(b[i]) // c, abs(a[i]) // c, z), 0) + 1
    else:
        if b[i] == 0:
            w += 1
mx = 0
for c in d:
    x = d[c]

    if x > mx:
        mx = x
print(int(mx) + w)
