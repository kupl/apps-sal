n = int(input())
p = [0,0] + [int(w) for w in input().split()]
d = [0] * (n+1)

for i in range(n, 1, -1):
    if d[i] == 0:
        d[i] = 1
    d[p[i]] += d[i]
if n == 1:
    d[1] = 1
d = d[1:]
d.sort()
print(*d)
