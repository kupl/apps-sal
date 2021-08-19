USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def check(s):
    (i, j) = (0, len(s) - 1)
    while i < j:
        if abs(ord(s[i]) - ord(s[j])) not in [0, 2]:
            return False
        (i, j) = (i + 1, j - 1)
    return True


def main():
    (T,) = list(map(int, input().split(' ')))
    for _ in range(T):
        (n,) = list(map(int, input().split(' ')))
        s = input()
        print(['NO', 'YES'][check(s)])


def __starting_point():
    main()


__starting_point()
