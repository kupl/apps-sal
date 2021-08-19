for i in range(int(input())):
    (l, r) = list(map(int, input().split()))
    if l == r:
        print((-1) ** (l % 2) * l)
    elif l % 2 == 1 and r % 2 == 0:
        print((r - l + 1) // 2)
    elif l % 2 == 1 and r % 2 == 1:
        print((r - l) // 2 - r)
    elif l % 2 == 0 and r % 2 == 0:
        print((r - l) // 2 + l)
    elif l % 2 == 0 and r % 2 == 1:
        print((r - l - 1) // 2 + l - r)
