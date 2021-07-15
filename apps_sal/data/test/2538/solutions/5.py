for cas in range(int(input())):
    a, b, c = map(int, input().split())
    l = (b + c - a) // 2 + 1
    r = c
    print(max(0, r - max(l, 0) + 1))
