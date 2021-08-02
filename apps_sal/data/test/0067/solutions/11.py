import sys
input = sys.stdin.readline

x, y, z = map(int, input().split())

base = x - y

if base + z > 0 and base - z > 0:
    print('+')
elif base + z < 0 and base - z < 0:
    print('-')
elif base + z == 0 and base - z == 0:
    print('0')
else:
    print('?')
