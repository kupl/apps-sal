for i in range(int(input())):
    n = int(input())
    n = n
    ans = 0
    while n >= 2:
        ch = 2
        deff = 5
        while ch + deff <= n:
            ch += deff
            deff += 3
        ans += 1
        n -= ch
    print(ans)
