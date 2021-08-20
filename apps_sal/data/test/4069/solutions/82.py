(x, k, d) = map(int, input().split())
count = 0
local = x


def odd_or_eaven(x, d, k):
    if k % 2 == 0:
        print(abs(x))
    else:
        print(abs(x - d))


if abs(x) < abs(d):
    odd_or_eaven(x, d, k)
elif abs(x) - abs(k * d) > abs(d):
    print(abs(abs(x) - abs(k * d)))
else:
    mod = x % d
    temp = k - x // d
    odd_or_eaven(mod, d, temp)
