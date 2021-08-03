q = int(input())
for _ in range(q):
    k, n, a, b = list(map(int, input().split()))
    if b * n >= k:
        print(-1)
        continue
    L = 0
    R = n
    while R - L > 1:
        M = (L + R) // 2
        if a * M + b * (n - M) < k:
            L = M
        else:
            R = M
    if a * R + b * (n - R) < k:
        print(R)
    else:
        print(L)
