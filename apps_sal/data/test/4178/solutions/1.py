def main():
    n = int(input())
    h = list(map(int, input().split()))
    flag = True
    for i in range(n - 1):
        if h[i + 1] - h[i] == 0:
            continue
        elif h[i + 1] - h[i] >= 1:
            h[i + 1] = h[i + 1] - 1
        else:
            flag = False
    if flag:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
