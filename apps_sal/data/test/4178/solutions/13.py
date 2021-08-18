def main():
    N = int(input())

    h = [int(i) for i in input().split()]

    h0 = h[0] - 1
    ans = 'Yes'
    for i in range(1, N):
        if h0 < h[i]:
            h0 = h[i] - 1
        elif h0 > h[i]:
            ans = 'No'
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
