import sys
input = sys.stdin.readline
flush = sys.stdout.flush
for _ in range(int(input())):
    (h, c, t) = list(map(int, input().split()))
    m = h + c >> 1
    if t <= m:
        print(2)
        continue
    a = (h - t) // (2 * t - h - c)
    b = a + 1
    print(2 * a + 1 if 2 * t * (2 * a + 1) * (2 * b + 1) >= (2 * b + 1) * ((a + 1) * h + a * c) + (2 * a + 1) * ((b + 1) * h + b * c) else 2 * b + 1)
