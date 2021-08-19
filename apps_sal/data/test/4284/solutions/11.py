for _ in range(int(input())):
    (k, n, a, b) = list(map(int, input().split()))
    if k <= b * n:
        print(-1)
        continue
    L = 0
    R = n + 1
    while R - L > 1:
        mid = (R + L) // 2
        if mid * a + (n - mid) * b < k:
            L = mid
        else:
            R = mid
    print(L)
