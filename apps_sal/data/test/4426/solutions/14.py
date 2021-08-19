import sys
stdin = sys.stdin


def ip():
    return int(sp())


def lp():
    return list(map(int, stdin.readline().split()))


def sp():
    return stdin.readline().rstrip()


s = sp()
if s == 'SUN':
    print(7)
elif s == 'MON':
    print(6)
elif s == 'TUE':
    print(5)
elif s == 'WED':
    print(4)
elif s == 'THU':
    print(3)
elif s == 'FRI':
    print(2)
else:
    print(1)
