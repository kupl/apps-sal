def __starting_point():
    s = input()
    l = len(s)
    s = set(list(s))
    k = int(input())
    if l < k:
        print("impossible")
    else:
        if (k - len(s)) > 0:
            print(k - len(s))
        else:
            print(0)


__starting_point()
