def main():
    t, s, x = list(map(int, input().strip().split()))
    if x < t:
        print("NO")
    elif x == t + 1 and s != 1:
        print("NO")
    elif (x - t) % s == 0 or (x - t - 1) % s == 0:
        print("YES")
    else:
        print("NO")


def __starting_point():
    main()


__starting_point()
