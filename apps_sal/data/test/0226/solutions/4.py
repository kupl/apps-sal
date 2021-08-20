n = int(input())
a = list(map(int, input().split()))


def max_revenue(i, a):
    if i == len(a) - 1:
        return (a[-1], 0)
    before = max_revenue(i + 1, a)
    take = (a[i] + before[1], before[0])
    give = (before[0], a[i] + before[1])
    if take[0] > give[0]:
        return take
    else:
        return give


r = max_revenue(0, a)
print(r[1], r[0])
