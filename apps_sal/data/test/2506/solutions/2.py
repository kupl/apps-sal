from bisect import bisect_left, bisect_right
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    a[i] *= -1
a.sort()


def check(mid):
    mm = 0
    for i in range(n):
        if -(a[i] + a[0]) < mid:
            break
        mm += bisect_right(a, -(mid + a[i]))
    return mm


ok = 0
ng = 10 ** 10 + 7
while ng != ok + 1:
    mid = (ok + ng) // 2
    if check(mid) >= m:
        ok = mid
    else:
        ng = mid
b = [0]
for i in a:
    b.append(b[-1] + i)
ans = 0
for i in range(n):
    if -(a[i] + a[0]) < ok:
        break
    ind = bisect_right(a, -(ok + a[i]))
    ans += a[i] * ind
    ans += b[ind]
print(-(ans + (check(ok) - m) * ok))
