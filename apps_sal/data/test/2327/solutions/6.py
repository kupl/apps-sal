for _ in range(int(input())):
    ans = 0
    n = int(input())
    x = 1
    while n:
        ans += ((n + 1) // 2) * x
        x += 1
        n -= ((n + 1) // 2)
    print(ans)
