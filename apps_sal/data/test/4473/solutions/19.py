for i in range(int(input())):
    (a, b, k) = map(int, input().split())
    if k == 0:
        print(0)
        continue
    if k % 2 == 0:
        print(a * (k // 2) - b * (k // 2))
    else:
        print(a * (k // 2 + 1) - b * (k // 2))
