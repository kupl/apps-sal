a, b = map(int, input().split())
c, d = map(int, input().split())

z = a * d - b * c
if z == 0:
    print(0)
    return
t = max(abs(a + b + c + d), abs(a + d - c - b), abs(a + c - b - d), abs(a + b - c - d))
print(abs(z / t))
