def c174(k):

    ans = -1
    sebun = 7

    for i in range(k):
        if sebun % k == 0:
            ans = i + 1
            return ans
        sebun = (sebun % k) * 10 + 7
    return ans


def main():
    k = int(input())
    print(c174(k))


def __starting_point():
    main()


__starting_point()
