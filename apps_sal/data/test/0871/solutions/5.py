n, s = map(int, input().split())
a, b = map(int, input().split())
if a * 60 + b >= s + 1:
    print(0, 0)
else:
    X = 0
    for i in range(n - 1):
        c, d = map(int, input().split())
        if c * 60 + d - (a * 60 + b) >= 2 * s + 2:
            M = a * 60 + b + 1 + s
            print(M // 60, M % 60)
            X = 1
            break
        else:
            a, b = c, d
    if X == 0:
        M = a * 60 + b + 1 + s
        print(M // 60, M % 60)
