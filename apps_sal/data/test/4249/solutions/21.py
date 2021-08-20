(n, m) = (int(t) for t in input().split(' '))
a = [int(t) for t in input().split(' ')]
a.sort(reverse=True)


def possible(d):
    total = 0
    for i in range(d):
        step = 0
        for j in range(i, n, d):
            total += max(a[j] - step, 0)
            step += 1
    return total >= m


(l, r) = (0, n + 1)
while l < r:
    mid = (l + r) // 2
    if possible(mid):
        r = mid
    else:
        l = mid + 1
if possible(l):
    print(l)
else:
    print(-1)
