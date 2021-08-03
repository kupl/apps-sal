for _ in range(int(input())):
    a, b, c = map(int, input().split())
    total = 1 + (a + b + c) // 2
    print(max(0, a + c - max(total, a) + 1))
