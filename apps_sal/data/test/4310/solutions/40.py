c = list(map(int, input().split()))
d = sorted(c)
a = 0
a += d[1] - d[0]
a += d[2] - d[1]
print(a)
