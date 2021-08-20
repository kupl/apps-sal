(a, b) = map(int, input().split())
c = a
d = b
for i in range(a * b):
    if c < d:
        c = c + a
    elif d < c:
        d = d + b
    else:
        break
print(c)
