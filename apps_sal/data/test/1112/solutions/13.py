a, b, c = list(map(int, input().split()))
d, e, f = list(map(int, input().split()))
g, h, i = list(map(int, input().split()))
a = g + ((h - b) / 2)
i = c + ((b - h) / 2)
e = b + c - i

print(int(a), " ", b, " ", c)
print(d, " ", int(e), " ", f)
print(g, " ", h, " ", int(i))
