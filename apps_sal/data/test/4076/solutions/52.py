import math
(A, B, H, M) = list(map(int, input().split()))
x = H / 12 * 360 + M / 60 * 30
y = M / 60 * 360
ang = abs(y - x)
ans_2 = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(ang))
ans = math.sqrt(ans_2)
print(ans)
