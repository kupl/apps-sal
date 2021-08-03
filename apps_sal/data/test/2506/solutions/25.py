import bisect


def is_ok(a, target, m):
    num = 0
    for val in a:
        index = bisect.bisect_left(a, target - val)
        num += len(a) - index
    if num <= m:
        return True
    else:
        return False


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()

ok, ng = 10 ** 10, -1
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(a, mid, m):
        ok = mid
    else:
        ng = mid

rui = [0] * (n + 1)

for i in range(n):
    rui[i + 1] = rui[i] + a[i]

cnt = 0
ret = 0

for val in a:
    index = bisect.bisect_left(a, ok - val)
    num = len(a) - index
    cnt += num
    ret += (num * val) + (rui[-1] - rui[index])

ret += (m - cnt) * ng

print(ret)
