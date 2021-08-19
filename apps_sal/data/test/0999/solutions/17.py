from sys import stdin, stdout


def ri():
    return list(map(int, input().split()))


n = int(input())
minnr = 10 ** 9 + 1
maxnl = -1
minmr = 10 ** 9 + 1
maxml = -1
for i in range(n):
    (l, r) = ri()
    minnr = min(minnr, r)
    maxnl = max(maxnl, l)
m = int(input())
for i in range(m):
    (l, r) = ri()
    minmr = min(minmr, r)
    maxml = max(maxml, l)
ans = 0
if minnr <= maxml:
    ans = maxml - minnr
else:
    ans = 0
if minmr <= maxnl:
    ans = max(ans, maxnl - minmr)
print(ans)
