import math
(A, B, H, M) = map(int, input().split())
if H >= 12:
    H -= 12
choperminute = 360 / 60
tanperminute = 30 / 60
tankaku = H * 30 + tanperminute * M
chokaku = choperminute * M
if chokaku >= tankaku:
    angle = chokaku - tankaku
else:
    angle = tankaku - chokaku
if angle > 180:
    angle = 360 - angle
ansjyou = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle))
print(ansjyou ** 0.5)
