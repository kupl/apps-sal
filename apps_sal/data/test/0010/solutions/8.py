n = int(input())
d = n // 7
r = n % 7
u, v = d + d, d + d
if r == 6:
    u += 1
if r == 1:
    v += 1
if r > 1:
    v += 2
print(u, v)
