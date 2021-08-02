n = int(input())
a = list(map(int, input().split()))
a.sort()
l = a[-1]


def bigger(ind):
    nonlocal a, n, l
    if a[ind] > l / 2:
        return True
    else:
        return False


top = n
bottom = -1
while top - bottom > 1:
    mid = (top + bottom) // 2
    if bigger(mid):
        top = mid
    else:
        bottom = mid
if a[top] + a[bottom] > l or a[top] == l:
    print(l, a[bottom])
else:
    print(l, a[top])
