import sys
f = sys.stdin
a = [int(u) for u in f.readline().strip().split()]
a.sort(reverse=True)
t = a[2]
dt = min(a[0] - a[1], 2 * t) // 2
a[2] -= dt
a[0] -= 2 * dt
a[0] -= a[2]
a[1] -= a[2]
t += min((a[0] + a[1]) // 3, a[1])
print(t)
