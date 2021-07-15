from itertools import count

n, m = list(map(int, input().split()))
p = [int(num) for num in input().split()]


def calc(cnt):
    new_p = list(map(lambda ind, num: num + cnt * ind, count(1), p))
    return sum(sorted(new_p)[:cnt])


def can(cnt):
    return calc(cnt) <= m


l = 0
r = n + 1
while r - l > 1:
    mid = (l + r) // 2
    if can(mid):
        l = mid
    else:
        r = mid

print(l, calc(l))

