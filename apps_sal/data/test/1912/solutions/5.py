import sys
input = sys.stdin.readline
t = int(input())


def check(r, g, b, w):
    if r >= 0 and g >= 0 and (b >= 0) and (w >= 0):
        c = 0
        if r % 2 != 0:
            c += 1
        if g % 2 != 0:
            c += 1
        if b % 2 != 0:
            c += 1
        if w % 2 != 0:
            c += 1
        if c == 0 or c == 1:
            return True
    return False


for t1 in range(t):
    (r, g, b, w) = list(map(int, input().split(' ')))
    if check(r, g, b, w) or check(r - 1, g - 1, b - 1, w + 1):
        print('Yes')
    else:
        print('No')
