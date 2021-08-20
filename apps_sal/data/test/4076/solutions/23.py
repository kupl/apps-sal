import math
(A, B, H, M) = list(map(int, input().split()))
if H == 0:
    H = 12
elif M == 0:
    M = 60
L = M / 5
N = min(abs(L - H), abs(H - L))
if L >= H:
    if M == 60:
        M = 0
    S = 360 * N / 12 - 0.5 * M
else:
    S = 360 * N / 12 + 0.5 * M
ANS = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(S))
ANS = math.sqrt(ANS)
print(ANS)
