from sys import stdin, stderr
(n, h) = list(map(int, stdin.readline().split()))
a = list(map(int, stdin.readline().split()))


def ok(k):
    b = list(sorted(a[:k], reverse=True))
    t = sum(b[::2])
    return t <= h


l = 0
r = n + 1
while r - l > 1:
    mid = (l + r) // 2
    if ok(mid):
        l = mid
    else:
        r = mid
print(l)
