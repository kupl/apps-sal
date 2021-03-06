from bisect import bisect_left
(n, m) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
maxA = max(A)
cnt = [0] * (maxA * 2 + 2)
rui = [n] * (maxA * 2 + 2)
for a in A:
    cnt[a] += 1
accum = 0
for i in range(maxA * 2 + 1):
    accum += cnt[i]
    rui[i + 1] -= accum


def f(x):
    ret = 0
    for left in A:
        ret += rui[max(x - left, 0)]
    return ret


lo = 0
hi = maxA * 2 + 1
while hi - lo > 1:
    md = (lo + hi) // 2
    if f(md) >= m:
        lo = md
    else:
        hi = md
ruiA = [0] * (n + 1)
for i in range(n):
    ruiA[i + 1] = ruiA[i] + A[i]
ans = 0
cnt = 0
for i in range(n):
    pos = bisect_left(A, lo - A[i])
    cnt += n - pos
    ans += ruiA[-1] - ruiA[pos] + A[i] * (n - pos)
if cnt == m:
    print(ans)
else:
    rem = cnt - m
    print(ans - rem * lo)
