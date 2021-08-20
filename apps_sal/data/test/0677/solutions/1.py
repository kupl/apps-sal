for _ in range(int(input())):
    (l, r, d) = list(map(int, input().split()))
    if l <= d and d <= r:
        x = r - r % d
        print(x + d)
    else:
        print(d)
