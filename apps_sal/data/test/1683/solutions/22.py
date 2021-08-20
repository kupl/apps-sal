def le2(num):
    s = str(num)
    ans = ''
    for i in s:
        ans += i + '0'
    ans = ans[:-1]
    return int(ans)


def m1(num, less):
    sn = str(num)
    sr = ''
    for i in range(less):
        sr += '0' + sn[-1]
        sn = sn[:-1]
    sr = sn + sr[::-1]
    return int(sr)


def m2(num, less):
    sn = str(num)
    sr = ''
    for i in range(less):
        sr += sn[-1] + '0'
        sn = sn[:-1]
    sr = sn + sr[::-1]
    return int(sr)


mod = 998244353
ans = 0
n = int(input())
d = [[] for i in range(11)]
a = list(map(int, input().split()))
for i in a:
    d[len(str(i))].append(i)
prev = 0
for i in range(1, 11):
    curlen = len(d[i])
    for lessnum in d[i - 1]:
        prev = (prev + le2(lessnum)) % mod
    ans = (ans + prev * curlen) % mod
    for lessdigits in range(1, i):
        downsum = 0
        for curnum in d[i]:
            downsum = (downsum + m1(curnum, lessdigits)) % mod
        ans = ans + downsum * len(d[lessdigits])
    cursuml1 = 0
    for enum in d[i]:
        res = le2(enum)
        ans = (ans + curlen * 11 * res) % mod
        cursuml1 = (cursuml1 + 10 * res) % mod
    for moredigits in range(i + 1, 11):
        ans = (ans + cursuml1 * len(d[moredigits])) % mod
        moresum = 0
        for morenum in d[moredigits]:
            moresum = (moresum + m2(morenum, i)) % mod
        ans = (ans + moresum * curlen) % mod
print(ans)
