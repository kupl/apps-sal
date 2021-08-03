def main():
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    cnt = [0] * (10**6 + 5)
    ans = 0
    for ai in a:
        j, x = 2, ai
        while x <= 10**6:
            if j == 2 and cnt[x] >= 1:
                cnt[x] += 1
                break
            cnt[x] += 1
            x = ai * j
            j += 1

    for ai in a:
        if cnt[ai] <= 1:
            ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
