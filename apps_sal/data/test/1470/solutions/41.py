

def main():
    x = int(input())
    ans, mod = divmod(x, 11)
    ans *= 2
    if mod >= 7:
        ans += 2
    elif mod > 0:
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
