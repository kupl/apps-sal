def main():
    nm = int(input())
    m = list(map(int, input().split()))
    nw = int(input())
    w = list(map(int, input().split()))
    m.sort()
    w.sort()
    i = j = ans = 0
    while i < nm and j < nw:
        if -1 <= m[i] - w[j] <= 1:
            ans += 1
            i += 1
            j += 1
        elif m[i] > w[j]:
            j += 1
        else:
            i += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
