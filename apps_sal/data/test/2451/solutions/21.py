USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    (n, h, a, b, k) = list(map(int, input().split(' ')))
    for _ in range(k):
        (ta, fa, tb, fb) = list(map(int, input().split(' ')))
        if ta == tb:
            ans = abs(fa - fb)
        else:
            ans = abs(ta - tb)
            if fa > fb:
                (fa, fb) = (fb, fa)
            if a <= fa <= b or fa <= a <= fb:
                ans += fb - fa
            elif fa >= b:
                ans += fa - b + fb - b
            elif fb <= a:
                ans += a - fa + a - fb
        print(ans)


def __starting_point():
    main()


__starting_point()
