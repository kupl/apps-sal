def getprint(c1, c2, c3, maxi, ost, delta):
    ans = str(maxi) + '\n' + (c1 * maxi + '\n') * ost
    return ans + (c2 * delta + c3 * (maxi - delta) + '\n') * (maxi - ost)


def solve():
    a = list(map(int, input().split()))
    if max(a) ** 2 != a[0] * a[1] + a[2] * a[3] + a[4] * a[5]:
        return -1
    maxi = max(a)
    if maxi in a[:2] and maxi in a[2:4] and (maxi in a[4:]):
        return str(maxi) + '\n' + ('A' * maxi + '\n') * min(a[:2]) + ('B' * maxi + '\n') * min(a[2:4]) + ('C' * maxi + '\n') * min(a[4:])
    ind = a.index(maxi)
    ost = a[ind ^ 1]
    if ind // 2 == 0 and maxi - ost in a[2:4] and (maxi - ost in a[4:]):
        return getprint('A', 'B', 'C', maxi, ost, a[2] * a[3] // (maxi - ost))
    elif ind // 2 == 1 and maxi - ost in a[:2] and (maxi - ost in a[4:]):
        return getprint('B', 'A', 'C', maxi, ost, a[0] * a[1] // (maxi - ost))
    elif ind // 2 == 2 and maxi - ost in a[:2] and (maxi - ost in a[2:4]):
        return getprint('C', 'A', 'B', maxi, ost, a[0] * a[1] // (maxi - ost))
    return -1


print(solve())
