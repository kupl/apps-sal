for i in range(int(input())):
    a, b = list(map(int, input().split()))
    a = -min(a, b) + max(a, b)
    ans = 0
    ans = a // 5
    a %= 5
    ans += a // 2
    a %= 2
    ans += a
    print(ans)
