import math
a, b, x = list(map(int, input().split()))

h = x / a / a
A = h * a

if A <= b * a / 2:
    L = A / b * 2
    ans = math.degrees(math.atan(b / L))
else:
    L = A * 2 / a - b
    ans = math.degrees(math.atan((b - L) / a))

print(ans)
