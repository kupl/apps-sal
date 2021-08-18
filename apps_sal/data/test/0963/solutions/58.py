import sys
import collections as cl
import bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9 + 7
Max = sys.maxsize


def l():
    return list(map(int, input().split()))


def m():
    return list(map(int, input().split()))


def onem():
    return int(input())


def s(x):
    a = []
    if len(x) == 0:
        return []
    aa = x[0]
    su = 1
    for i in range(len(x) - 1):
        if aa != x[i + 1]:
            a.append([aa, su])
            aa = x[i + 1]
            su = 1
        else:
            su += 1
    a.append([aa, su])
    return a


def jo(x):
    return " ".join(map(str, x))


def max2(x):
    return max(list(map(max, x)))


def In(x, a):
    k = bs.bisect_left(a, x)
    if k != len(a) and a[k] == x:
        return True
    else:
        return False


def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans


"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

n, k = m()
mod = 998244353
ans = [0 for i in range(n + 1)]

data = []
for i in range(k):
    data.append(l())

for i in range(0, n):
    if i == 0:
        ans[i] = 1
    else:
        ans[i] += ans[i - 1]
        ans[i] %= mod
        for j in range(k):
            l, r = data[j]
            r += 1
            if l + i <= n:
                ans[i + l] += ans[i]
                ans[i + l] %= mod
            if r + i <= n:
                ans[i + r] -= ans[i]
                ans[i + r] %= mod

print((ans[-1]))
