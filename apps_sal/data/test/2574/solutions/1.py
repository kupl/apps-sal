t = int(input())
for _ in range(t):
    n = int(input())
    k = sorted(map(int, input().strip().split()))
    (a, b) = (k[0] * k[1], k[2] * k[3])
    (c, d) = (k[-5] * k[-4], k[-3] * k[-2])
    e = k[-1]
    print(max(a * b * e, a * d * e, c * d * e))
