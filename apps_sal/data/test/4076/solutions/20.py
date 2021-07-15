import math

a, b, h, m = map(int, input().split())
angle = ((h * 60 + m) / 720 - m / 60) * math.pi * 2  # 角度(ラジアン)
ans = math.sqrt(a*a + b*b - 2*a*b*math.cos(angle))  # 余弦定理
print(ans)
