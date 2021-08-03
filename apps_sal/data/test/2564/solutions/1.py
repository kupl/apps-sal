for _ in range(int(input())):
    a, b, n = list(map(int, input().split()))
    ans = 0
    a, b = min(a, b), max(a, b)
    while b <= n:
        a, b = b, a + b
        ans += 1
    print(ans)
