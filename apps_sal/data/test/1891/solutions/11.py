from bisect import bisect_left, bisect_right

n, k, a, b = [int(x) for x in input().split()]
pos = [int(x) for x in input().split()]
na = {}
v = {}
for i in pos:
    na[i] = na.get(i, 0) + 1
    v[i] = b * na[i]
l = 2
t = 2
while t <= n + 1:
    xna = {}
    for i in na:
        j = (i + 1) // 2
        xna[j] = xna.get(j, 0) + na[i]
    na = xna
    xv = {}
    for i in na:
        j = i * 2
        xv[i] = min(b * na[i] * l, v.get(j - 1, a) + v.get(j, a))
    v = xv
    l *= 2
    t += 1
print(v[1])
