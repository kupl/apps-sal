
def main():
    s, t = input().split(" ")
    a, b = map(int, input().split(" "))
    u = input()
    if u == s:
        a -= 1
    else:
        b -= 1
    print(f"{a} {b}")


def __starting_point():
    main()


__starting_point()
