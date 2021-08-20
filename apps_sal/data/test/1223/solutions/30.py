import sys
stdin = sys.stdin


def ni():
    return int(ns())


def nl():
    return list(map(int, stdin.readline().split()))


def nm():
    return list(map(int, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


n = ni()
p = nl()
q = [0] * (n + 1)
for i in range(n):
    q[p[i]] = i + 1
ans = 0
l = [0] + [i for i in range(n + 1)]
r = [i + 1 for i in range(n + 1)] + [n + 1]
for i in range(1, n + 1):
    v = q[i]
    (l1, r1) = (l[v], r[v])
    (l2, r2) = (l[l1], r[r1])
    ans += i * ((v - l1) * (r2 - r1) + (r1 - v) * (l1 - l2))
    l[r1] = l1
    r[l1] = r1
print(ans)
