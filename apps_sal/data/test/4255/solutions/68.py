from math import sqrt
a, b, c = map(int, input().split())
s = (a + b + c) / 2
ans = sqrt(s * (s - a) * (s - b) * (s - c))
print(int(ans))
