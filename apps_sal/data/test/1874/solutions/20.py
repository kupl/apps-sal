import math
ns = [3, 4, 5]
L = list(map(int, input().split()))
PI = math.acos(-1)
ans = 0
for n, l in zip(ns, L):
    ang = PI / n
#    l / 2 / r = math.cos(ang)
    r = l / 2 / math.sin(ang)
    S = n * math.sin(2 * ang) * r * r / 2
    h = (l**2 - r**2)**0.5
#   print(S,h)
    ans += S * h / 3
print("%.10f" % (ans))
