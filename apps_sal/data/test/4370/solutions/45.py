import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = max(a, b)
d = min(a, b)
e = 16 - 2 * c
if e < 0:
    print(':(')
else:
    if e // 2 >= c - d:
        print('Yay!')
    else:
        print(':(')
