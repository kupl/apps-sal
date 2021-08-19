import sys


def resolve(in_):
    S = next(in_).strip()
    if S[0] != 'A':
        return False
    if S.count('C', 2, -1) != 1:
        return False
    i = S.find('C')
    a = S[1:i]
    b = S[i + 1:]
    if not (a.islower() and b.islower()):
        return False
    return True


def main():
    answer = resolve(sys.stdin)
    print('AC' if answer else 'WA')


def __starting_point():
    main()


__starting_point()
