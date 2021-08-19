for i in range(int(input())):
    (c, m, x) = map(int, input().split())
    print(min((c + m + x) // 3, min(c, m)))
