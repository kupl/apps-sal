for _ in range(int(input())):
    ans = 0
    n = int(input())
    cp = 1
    while cp * (cp + 1) // 2 <= n:
        ans += 1
        n -= cp * (cp + 1) // 2
        cp = cp * 2 + 1
    print(ans)
