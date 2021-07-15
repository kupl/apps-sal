def main():
    N, P = list(map(int, input().split()))
    *s, = list(map(int, input()))

    if P in {2, 5}:
        ans = 0
        for i, x in enumerate(reversed(s), start=0):
            if x % P == 0:
                ans += N - i
        print(ans)
        return

    ans = 0
    total = 0
    coef = 1
    ctr = [0] * P
    ctr[0] = 1
    for x in reversed(s):
        total = (total + x * coef) % P
        coef = coef * 10 % P
        ans += ctr[total]
        ctr[total] += 1
    print(ans)


def __starting_point():
    main()

__starting_point()
