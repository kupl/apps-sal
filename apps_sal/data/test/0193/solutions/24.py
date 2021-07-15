a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
z = a * d - b * c
if z == 0:
    print(0)
    return
t = max(abs(a + b + c + d), abs(a - b - c + d), abs(a - b + c - d), abs(a + b - c- d))
print(abs(z / t))

