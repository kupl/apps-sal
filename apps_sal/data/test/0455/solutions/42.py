from functools import reduce
import math

n = int(input())
coord = [tuple(map(int, input().split())) for i in range(n)]

# parity check and get max
x, y = coord[0]
p = (x + y) & 1
limit = 0
for x, y in coord:
    if p != (x + y) & 1:
        print(-1)
        return
    lim = abs(x) + abs(y)
    if lim > limit:
        limit = lim

limit = round(math.log2(limit))
if p == 1:
    d = [2 ** i for i in reversed(range(limit + 1))]
else:
    d = [1] + [2 ** i for i in reversed(range(limit + 1))]

print(len(d))
print(reduce((lambda acc, dist: str(acc) + " " + str(dist)), d))

for x, y in coord:
    u = x + y
    v = x - y

    command = ""
    for i in range(len(d)):
        if u >= 0 and v >= 0:
            command += "R"
            u -= d[i]
            v -= d[i]
        elif u >= 0 > v:
            command += "U"
            u -= d[i]
            v += d[i]
        elif u < 0 <= v:
            command += "D"
            u += d[i]
            v -= d[i]
        elif u < 0 and v < 0:
            command += "L"
            u += d[i]
            v += d[i]

    print(command)
