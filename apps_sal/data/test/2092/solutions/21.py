from sys import stdin

input = stdin.readline

m, n, k, t = list(map(int, input().split()))

a = list(map(int, input().split()))

trap = []


def check(x):
    avg = a[-x]
    cost = n + 1
    nr = 0
    for i in range(k):
        xx, y, d = trap[i]
        if d <= avg:
            continue
        if y > nr:
            cost += (y - max(xx - 1, nr)) * 2
            nr = y
    return cost <= t


for i in range(k):
    trap.append(list(map(int, input().split())))

trap.sort()
a.sort()

l = 0
r = m + 1

while r - l > 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid


print(l)
