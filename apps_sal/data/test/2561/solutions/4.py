USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def count_bits(x):
    ans = 0
    while x:
        ans += 1
        x &= x - 1
    return ans


def main():
    (t,) = list(map(int, input().split(' ')))
    for _ in range(t):
        (a,) = list(map(int, input().split(' ')))
        c = count_bits(a)
        ans = 1 << c
        print(ans)


def __starting_point():
    main()


__starting_point()
