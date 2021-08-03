for _ in range(int(input())):
    n = int(input())

    i = 1
    have = 0
    ans = 0
    while have + i * (i + 1) // 2 <= n:
        have += i * (i + 1) // 2
        ans += 1
        i = i * 2 + 1

    print(ans)
