import sys

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    S = input()
    ch = ord('a')

    for c in S:
        if ord(c) > ch:
            print('NO')
            return
        elif ord(c) == ch:
            ch += 1
        else:
            pass
    
    print('YES')


def __starting_point():
    solve()
__starting_point()
