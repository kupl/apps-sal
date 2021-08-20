for i in range(int(input())):
    (l, r, d) = map(int, input().split())
    if l > d:
        print(d)
    else:
        j = r - r % d + d
        print(j)
