import sys
sys.setrecursionlimit(10 ** 6)
(x, y) = list(map(str, input().split()))
x = int('0x' + x, 16)
y = int('0x' + y, 16)
if x > y:
    print('>')
elif x == y:
    print('=')
else:
    print('<')
