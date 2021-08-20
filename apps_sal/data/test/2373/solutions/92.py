def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for (i, q) in enumerate(p):
        if q == i + 1:
            cnt += 1
            if cnt == 3:
                cnt = 1
                ans += 1
        else:
            if cnt == 0:
                continue
            cnt = 0
            ans += 1
    if cnt in [1, 2]:
        ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
