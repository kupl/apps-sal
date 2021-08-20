(N, A, B) = map(int, input().split())
H = [int(input()) for n in range(N)]
L = 0
R = 10 ** 9
while 1 < R - L:
    m = (L + R) // 2
    if m < -sum((min(0, (h - m * B) // (B - A)) for h in H)):
        L = m
    else:
        R = m
print(R)
