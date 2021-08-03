
def main():
    N, P = list(map(int, input().split()))
    s = list(input())[::-1]
    ary_mod = [0] * P
    ary_mod[0] = 1
    now = 0
    digit = 1
    ans = 0
    if P == 2:
        for i, ss in enumerate(s):
            if int(ss) % 2 == 0:
                ans += N - i
        print(ans)
        return
    if P == 5:
        for i, ss in enumerate(s):
            if int(ss) % 5 == 0:
                ans += N - i
        print(ans)
        return

    for i, ss in enumerate(s):
        now += int(ss) * digit % P
        digit *= 10
        digit %= P
        remind = now % P
        ary_mod[remind] += 1
    ans = 0
    for i, n in enumerate(ary_mod):
        ans += (n * (n - 1)) // 2
    print(ans)


def __starting_point():
    main()


__starting_point()
