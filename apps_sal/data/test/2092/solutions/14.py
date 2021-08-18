import sys


def army(weak, traps, t_max, n):
    t = n + 1
    alone = [0] * (n + 1)
    for l, r, d in traps:
        if d <= weak:
            break
        alone[l - 1] += 1
        alone[r] -= 1

    interval = 0
    for loc in range(n + 1):
        interval += alone[loc]
        if interval:
            t += 2

    return t <= t_max


reader = (list(map(int, s.split())) for s in sys.stdin)

m, n, k, t_max = next(reader)
a = list(next(reader))
traps = []
for _ in range(k):
    l, r, d = next(reader)
    traps.append((l, r, d))

a.sort(reverse=True)
traps.sort(key=lambda x: x[2], reverse=True)

L = 0
R = m + 1
while L + 1 < R:
    check = (L + R) // 2
    if army(a[check - 1], traps, t_max, n):
        L = check
    else:
        R = check

print(L)
