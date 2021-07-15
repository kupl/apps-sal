def main():
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    mi, ma = min(l), max(l)
    if ma - mi > k:
        print('NO')
        return
    print('YES')
    res = ['1'] * (mi + 1)
    for i in range(2, k + 1):
        res.append(str(i))
    for a in l:
        print(' '.join(res[:a]))


def __starting_point():
    main()

__starting_point()
