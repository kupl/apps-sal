n, k, *a = list(map(int, open(0).read().split()))


def c(x):
    res = 0
    for b in a:
        # bを最大がxになるように、できるだけ少ない回数で
        # だいたいb/x等分？
        res += 0 - - b // x - 1
    return res <= k


ng = 0
ok = 10 ** 10
while ok - ng > 1:
    mid = (ok + ng) >> 1
    if c(mid):
        ok = mid
    else:
        ng = mid
print(ok)

