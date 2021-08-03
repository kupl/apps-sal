n, S = list(map(int, input().split()))
a = [int(x) for x in input().split()]


def calc(k):
    prices = [a[i] + (i + 1) * k for i, x in enumerate(a)]
    prices.sort()
    return sum(prices[:k])


l, r = 0, n
while l != r:
    m = (l + r + 1) // 2
    if calc(m) <= S:
        l = m
    else:
        r = m - 1

print(l, calc(l))
