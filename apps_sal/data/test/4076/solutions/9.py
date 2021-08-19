import math
x = list(map(int, input().split()))
A = x[0]
B = x[1]
H = x[2]
M = x[3]
y = 2 * math.pi * ((H * 60 + M) / 720 - M / 60)
z = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(y))
print(z)
