import math
(n, r) = (int(x) for x in input().split())
s = math.sin(math.pi / n)
ans = r * s / (1 - s)
print('%.7f' % ans)
