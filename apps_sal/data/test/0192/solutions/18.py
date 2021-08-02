import math

x, y = list(map(int, input().split()))
res = 0
now = [y, y, y]
while min(now) < x:
    res += 1
    ind = now.index(min(now))
    o1, o2 = (ind + 1) % 3, (ind + 2) % 3
    now[ind] = now[o1] + now[o2] - 1
print(res)
