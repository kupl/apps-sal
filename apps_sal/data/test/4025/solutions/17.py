import collections


def calc(day, a, b, c):
    ret = 0
    while True:
        if a > 300000000 and b > 200000000 and (c > 200000000):
            a -= 300000000
            b -= 200000000
            c -= 200000000
            ret += 700000000
        elif a > 3000000 and b > 2000000 and (c > 2000000):
            a -= 3000000
            b -= 2000000
            c -= 2000000
            ret += 7000000
        elif a > 30000 and b > 20000 and (c > 20000):
            a -= 30000
            b -= 20000
            c -= 20000
            ret += 70000
        elif a > 300 and b > 200 and (c > 200):
            a -= 300
            b -= 200
            c -= 200
            ret += 700
        elif a > 3 and b > 2 and (c > 2):
            a -= 3
            b -= 2
            c -= 2
            ret += 7
        else:
            break
    while True:
        if day == 0 or day == 3 or day == 6:
            a -= 1
            if a < 0:
                return ret
        elif day == 1 or day == 5:
            b -= 1
            if b < 0:
                return ret
        elif day == 2 or day == 4:
            c -= 1
            if c < 0:
                return ret
        ret += 1
        day = (day + 1) % 7


def solve():
    (a, b, c) = list(map(int, input().split()))
    ans = 0
    for i in range(7):
        ans = max(ans, calc(i, a, b, c))
    return ans


print(solve())
