__author__ = 'zhan'

[n, x, y] = [int(i) for i in input().split()]
inpu = [0] * n
for i in range(n):
    inpu[i] = int(input())
ox = x
oy = y
loop = x + y
hits = [2]*(loop+1)
i = 1
while i <= loop:
    if y < x:
        hits[i] = 0
        y += oy
        i += 1
    elif x < y:
        hits[i] = 1
        x += ox
        i += 1
    else:
        hits[i] = 2
        hits[i+1] = 2
        x += ox
        y += oy
        i += 2
final = [""] * n
i = 0
for inp in inpu:
    k = inp % loop
    if hits[k] == 0:
        final[i] = "Vanya"
    elif hits[k] == 1:
        final[i] = "Vova"
    else:
        final[i] = "Both"
    i += 1

print("\n".join(final))

