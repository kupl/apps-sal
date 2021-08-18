n = int(input())
m = list(int(x) for x in input().split())
m = [0] + m
d = 0
c = 0
e = 0
p = 0
for i in range(0, n):
    t = m[i] - m[i + 1]
    if (e + t) > 0:
        e += t
    else:
        c += abs(e + t)
        e = 0
print(c)
