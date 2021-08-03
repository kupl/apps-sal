n = int(input())
x = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]


def fin(h):
    return max(abs(h - x[i]) / v[i] for i in range(n))


l, r = 1.0, 1e9
while r - l > 5e-7:
    mid = (l + r) / 2
    if (fin(mid - 4e-7) < fin(mid + 4e-7)):
        r = mid
    else:
        l = mid

print(fin(l))
