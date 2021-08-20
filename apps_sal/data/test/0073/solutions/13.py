(c, v0, v1, a, l) = map(int, input().split())
x = 0
i = 0
while x < c:
    x += min(v0 + a * i, v1) - l * (i > 0)
    i += 1
print(i)
