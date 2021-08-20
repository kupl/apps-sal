from bisect import bisect_right
n = int(input())
a = sorted(list(map(int, input().split())))
x = a[-1]
c = bisect_right(a, x // 2)
if x % 2 == 0:
    if x // 2 in a:
        print('{} {}'.format(x, x // 2))
    elif a[c] - x // 2 >= x // 2 - a[c - 1]:
        print('{} {}'.format(x, a[c - 1]))
    else:
        print('{} {}'.format(x, a[c]))
elif x // 2 in a:
    print('{} {}'.format(x, x // 2))
elif x // 2 + 1 in a:
    print('{} {}'.format(x, x // 2 + 1))
elif a[c] - (x // 2 + 1) >= x // 2 - a[c - 1]:
    print('{} {}'.format(x, a[c - 1]))
else:
    print('{} {}'.format(x, a[c]))
