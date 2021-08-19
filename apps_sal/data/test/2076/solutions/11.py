for _ in range(int(input())):
    (a, b, c) = list(map(int, input().split()))
    c2 = min(c // 2, b)
    print((c2 + min((b - c2) // 2, a)) * 3)
