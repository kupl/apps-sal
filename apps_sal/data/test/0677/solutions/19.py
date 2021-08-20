for _ in range(int(input())):
    (l, r, d) = list(map(int, input().split()))
    if d < l:
        print(d)
    else:
        k = r // d
        print((k + 1) * d)
