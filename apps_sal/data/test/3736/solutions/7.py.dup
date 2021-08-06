import sys


def check(text):
    legal = 'AHIMOTUVWXY'
    for i in text:
        if i not in legal:
            return False
    rev = list(text)
    rev.reverse()
    if text != ''.join(rev):
        return False
    return True


def __starting_point():
    text = sys.stdin.readline().split()[0]
    if check(text):
        print('YES')
    else:
        print('NO')


__starting_point()
