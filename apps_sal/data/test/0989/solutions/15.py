from sys import stdin

n, k = [int(i) for i in stdin.readline().strip().split()]
a = [int(i) for i in stdin.readline().strip().split()]
a.sort()

ups = n * [0]
downs = n * [0]

for i in range(0, n - 1):
    ups[i + 1] = ups[i] + (i + 1) * (a[i + 1] - a[i])

for i in range(n - 1, 0, -1):
    downs[i - 1] = downs[i] + (n - i) * (a[i] - a[i - 1])


def find_max(steps):
    """Lowest possible maximum reachable for given number of steps"""
    l, r = 0, n - 1
    x = None
    while l <= r:
        m = (l + r) // 2
        if downs[m] <= steps:
            x = m
            r = m - 1
        else:
            l = m + 1

    value = a[x]
    if x > 0 and downs[x] < steps:
        value -= (steps - downs[x]) // (n - x)

    return value


def find_min(steps):
    l, r = 0, n - 1
    x = None
    while l <= r:
        m = (l + r) // 2
        if ups[m] <= steps:
            x = m
            l = m + 1
        else:
            r = m - 1

    value = a[x]
    if x < n:
        value += (steps - ups[x]) // (x + 1)

    return value


best_diff = a[-1] - a[0]
for i in range(n):
    if ups[i] > k:
        break
    min_a = a[i]
    max_a = find_max(k - ups[i])
    if max_a <= min_a:
        best_diff = 0
        break
    best_diff = min(best_diff, max_a - min_a)

for i in range(n - 1, -1, -1):
    if best_diff == 0:
        break
    if downs[i] > k:
        break
    max_a = a[i]
    min_a = find_min(k - downs[i])
    if min_a >= max_a:
        best_diff = 0
        break
    best_diff = min(best_diff, max_a - min_a)

print(best_diff)
