import math


def mi():
    return list(map(int, input().split()))


'''
3
10 4 5 2
5 1 3 4
20 4 19 3
'''
for _ in range(int(input())):
    n, x, y, d = mi()
    if abs(x - y) % d == 0:
        print(abs(x - y) // d)
    else:
        ans1 = math.ceil((x - 1) / d)
        ans2 = math.ceil((n - x) / d)
        if abs(y - 1) % d == 0:
            ans1 += (y - 1) // d
        else:
            ans1 = 1e19
        if abs(n - y) % d == 0:
            ans2 += (n - y) // d
        else:
            ans2 = 1e19
        if min(ans1, ans2) == 1e19:
            print(-1)
        else:
            print(min(ans1, ans2))
