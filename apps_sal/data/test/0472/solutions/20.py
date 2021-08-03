import math


def digit_sum(num):
    res = 0
    while num:
        res += num % 10
        num //= 10
    return res


def R(): return map(int, input().split())


n = int(input())
res = math.inf
for s in range(1, 91):
    l, r = 1, 10**9
    while l < r:
        x = (l + r) // 2
        ne = x * x + s * x
        if ne < n:
            l = x + 1
        elif ne > n:
            r = x - 1
        else:
            l = r = x
            break
    if l * (l + digit_sum(l)) == n:
        res = min(l, res)
print(res if res < math.inf else -1)
