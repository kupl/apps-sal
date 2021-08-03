for q in range(int(input())):
    c, m, x = list(map(int, input().split()))
    a = min(c, m, (c + m + x) // 3)
    print(a)
