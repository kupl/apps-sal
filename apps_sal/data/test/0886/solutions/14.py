def main():
    n = input()
    l = len(n)
    ans = -1
    m = -1
    for i in range(l):

        if int(n[i]) % 2 == 0:
            ans = i

            if int(n[l - 1]) > int(n[i]):
                m = i
                break

    if ans == -1:
        print(-1)
    else:
        if m != -1:
            ans = m
        k = list(n)
        k[l - 1], k[ans] = k[ans], k[l - 1]
        print("".join(k))


def __starting_point():
    main()


__starting_point()
