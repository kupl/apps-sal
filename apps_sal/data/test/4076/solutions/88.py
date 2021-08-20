import math
(A, B, H, M) = map(int, input().split())
k = M / 60
if H == 0:
    H = 12
if M == 0:
    M = 60
H_d = (H / 12 * 60 + k * 5) / 60 * 2 * math.pi
M_d = M / 60 * 2 * math.pi
r = abs(H_d - M_d)
print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(r)))
