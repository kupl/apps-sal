import sys
stdin = sys.stdin

ip = lambda: int(sp())

lp = lambda: list(map(int, stdin.readline().split()))
sp = lambda: stdin.readline().rstrip()

s = sp()

if s == 'SUN':
    print((7))
elif s == 'MON':
    print((6))

elif s == 'TUE':
    print((5))
elif s == 'WED':
    print((4))
elif s == 'THU':
    print((3))

elif s == 'FRI':
    print((2))
else:
    print((1))
