def main():
    n, m = map(int, input().split())
    a = input().count('-')
    if a > n - a:
        a = n - a
    res = []
    for _ in range(m):
        l, r = map(int, input().split())
        r -= l
        res.append(('0', '1')[r & 1 and a * 2 >= r + 1])
    print('\n'.join(res))


def __starting_point():
    main()
__starting_point()
