def solve():
    (r, g, b, w) = list(map(int, input().split()))
    if min([r, g, b]) == 0:
        if r % 2 + g % 2 + b % 2 + w % 2 > 1:
            print('No')
        else:
            print('Yes')
    else:
        (r2, g2, b2, w2) = (r - 1, g - 1, b - 1, w + 3)
        if r2 % 2 + g2 % 2 + b2 % 2 + w2 % 2 > 1 and r % 2 + g % 2 + b % 2 + w % 2 > 1:
            print('No')
        else:
            print('Yes')


[solve() for x in range(int(input()))]
