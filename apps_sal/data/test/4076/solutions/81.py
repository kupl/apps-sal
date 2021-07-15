A, B, H, M = map(int, input().split())

# 時針: 12時間720分で360度 1分で0.5度
# 分針: 60分で360度 1分で6度
theta = abs(((0.5 * (H * 60 + M)) - (6 * M)) % 360)
if theta > 180:
  theta = 360 - theta
#print(theta)
import math
C = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta / 180 * math.pi))
print(C)
