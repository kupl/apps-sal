a, b, c, d = list(map(int, input().split()))
s = a * c
t = a * d
u = b * c
v = b * d
print((max(s, t, u, v)))
