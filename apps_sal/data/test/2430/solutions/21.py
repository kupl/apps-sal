def main():
    cur, val = 0, -1
    for i in range(int(input())):
        h = int(input())
        val += abs(cur - h) + 2
        cur = h
    print(val)


def __starting_point():
    main()
__starting_point()
