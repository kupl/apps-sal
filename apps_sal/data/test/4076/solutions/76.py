import math
(a, b, h, m) = list(map(int, input().split()))
ang = h * 30 - m * 5.5
ans = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(ang)))
print(ans)
