def main():
    N = int(input())
    (*H,) = list(map(int, input().split()))
    ans = 0
    cnt = 0
    prev = H[0] - 1
    for h in H:
        if h <= prev:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
        prev = h
    print(ans)


def __starting_point():
    main()


__starting_point()
