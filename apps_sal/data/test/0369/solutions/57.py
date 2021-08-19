def main():
    (n, m) = map(int, input().split())
    s = input().rstrip()
    ans = []
    x = n
    f = True
    while x > 0 and f:
        for i in reversed(range(m + 1)):
            if i == 0:
                f = False
                break
            if s[max(0, x - i)] == '0':
                if x - i < 0:
                    ans.append(x)
                else:
                    ans.append(i)
                x = max(0, x - i)
                break
    if f:
        for v in reversed(ans):
            print(v, end=' ')
        print('')
    else:
        print('-1')


def __starting_point():
    main()


__starting_point()
