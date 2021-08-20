for _ in range(int(input())):
    (a, b, k) = map(int, input().split())
    if a == b:
        print(0 if k % 2 == 0 else a)
    elif k % 2 == 1:
        print((k // 2 + 1) * a - k // 2 * b)
    else:
        print(k // 2 * a - k // 2 * b)
