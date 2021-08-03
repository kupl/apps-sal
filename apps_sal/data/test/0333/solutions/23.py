def __starting_point():
    a = input()
    b = input()
    if (a == b):
        print(-1)
    else:
        print(max(len(a), len(b)))


__starting_point()
