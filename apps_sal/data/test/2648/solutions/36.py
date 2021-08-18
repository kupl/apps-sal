from sys import stdin
from collections import Counter


def main():
    readline = stdin.readline
    n = int(readline())
    a = list(map(int, readline().split()))

    c = Counter(a)
    ans = n
    cnt_two = 0
    for key in c.keys():
        if c[key] >= 3:
            if c[key] % 2 == 1:
                ans -= c[key] - 1
                c[key] = 1
            else:
                ans -= c[key] - 2
                c[key] = 2
                cnt_two += 1
        elif c[key] == 2:
            cnt_two += 1

    if cnt_two % 2 == 0:
        ans -= cnt_two
    else:
        ans -= cnt_two - 1
        ans -= 2

    print(ans)


def __starting_point():
    main()


__starting_point()
