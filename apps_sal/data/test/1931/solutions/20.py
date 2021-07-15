for _ in range(int(input())):
    n = int(input())
    x = 0
    while (3 * x * x + x) // 2 < n:
        x += 1
    ans = 0
    while n > 1:
        if (3 * x * x + x) // 2 <= n:
            n = n - (3 * x * x + x) // 2
            ans += 1
        else:
            x -= 1
    print(ans)
