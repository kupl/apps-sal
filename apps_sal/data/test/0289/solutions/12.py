import sys


def solve():
    s = [ch for ch in input()]
    ans = ''.join(s).count('VK')

    for i in range(len(s)):
        if s[i] == 'V':
            s[i] = 'K'

            tmp = ''.join(s).count('VK')
            ans = max(ans, tmp)

            s[i] = 'V'
        else:
            s[i] = 'V'

            tmp = ''.join(s).count('VK')
            ans = max(ans, tmp)

            s[i] = 'K'

    print(ans)


def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None


def __starting_point():
    solve()


__starting_point()
