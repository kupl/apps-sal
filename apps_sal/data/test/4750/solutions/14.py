for i in range(int(input())):
    l, r, l1, r2 = map(int, input().split())
    if l == l1:
        print(l, l + 1)
    else:
        print(l, l1)
