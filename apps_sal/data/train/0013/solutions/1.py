for _ in range(int(input())):
    (n, g, b) = list(map(int, input().split()))
    half = (n - 1) // 2 + 1
    ans = (g + b) * (half // g) - b
    if half % g != 0:
        ans += b + half % g
    print(max(ans, n))
