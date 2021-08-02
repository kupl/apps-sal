n = int(input())
a = [int(i) for i in input().split()]
c = [0] * (n + 1)

for e in a:
    if e <= n:
        c[e] = 1
l = [e for e in range(1, n + 1) if c[e] == 0]

s = 0
c = [0] * (n + 1)
for i in range(n):
    if a[i] <= n and c[a[i]] < 1:
        c[a[i]] = 1
    else:
        a[i] = l[s]
        s += 1

for e in a:
    print(e, end=' ')
