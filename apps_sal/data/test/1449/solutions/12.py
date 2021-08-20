def solve():
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(1)
        return
    diff = 1
    ans = 1
    for (i, v) in enumerate(a):
        if i > 0:
            if v == a[i - 1]:
                continue
            else:
                diff += 1
                if diff > k:
                    ans += 1
                    diff = 2
    if diff > k:
        print(-1)
    else:
        print(ans)
    return


def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
