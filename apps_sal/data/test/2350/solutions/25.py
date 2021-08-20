for i in range(int(input())):
    (a, b, c, d) = list(map(int, input().split()))
    print((c - a) * (d - b) + 1)
