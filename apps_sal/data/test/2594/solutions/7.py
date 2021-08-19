for _ in range(int(input())):
    (n, m) = map(int, input().split())
    ans = n // 2 * m
    if n % 2 == 1:
        ans += m // 2
        if m % 2 == 1:
            ans += 1
    print(ans)
