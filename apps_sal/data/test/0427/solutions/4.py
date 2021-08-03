a, b, x, y = list(map(int, input().split()))
L, R = 0, 10 ** 18
while R - L > 1:
    M = (L + R) // 2
    if M - M // x < a or min(M - a - M // (x * y), M - M // y) < b:
        L = M
    else:
        R = M
print(R)
