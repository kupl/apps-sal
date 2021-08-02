def main():
    n, m = map(int, input().split())
    aa = list(map(int, input().split()))
    cnt = [True] * 100001
    res = []
    x = 0
    for a in reversed(aa):
        if cnt[a]:
            cnt[a] = False
            x += 1
        res.append(x)
    print('\n'.join(str(res[n - int(input())]) for _ in range(m)))


def __starting_point():
    main()


__starting_point()
