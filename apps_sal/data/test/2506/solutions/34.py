from bisect import bisect_left as bl
def ii(): return int(input())


def mi(): return list(map(int, input().split()))
def li(): return list(map(int, input().split()))


n, m = mi()
alis = li()

alis.sort()
ok = 0
ng = alis[n - 1] * 2 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    ima = 0
    for i in range(n):
        ima += n - bl(alis, mid - alis[i])
    if ima >= m:
        ok = mid
        outrange = ima - m
    else:
        ng = mid

acu_alis = [0] * n
ima = 0
for i in range(n):
    acu_alis[i] = alis[i] + ima
    ima = alis[i] + ima

ans = 0
for i in range(n):
    tmp = bl(alis, ok - alis[i])
    if tmp == 0:
        ans += n * alis[i] + acu_alis[n - 1]
    else:
        ans += (n - tmp) * alis[i] + acu_alis[n - 1] - acu_alis[tmp - 1]
ans -= outrange * ok
print(ans)
