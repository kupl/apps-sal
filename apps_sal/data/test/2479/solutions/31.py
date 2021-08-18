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
    return map(int, input().split())


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
    return max(map(max, x))


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


n, q = m()

ans = (n - 2)**2

ta = n - 2
tate = [n - 2 for i in range(n - 2)]
ltate = [0 for i in range(n - 2)]
yo = n - 2
yoko = [n - 2 for i in range(n - 2)]
lyoko = [0 for i in range(n - 2)]
for i in range(q):
    a, b = m()
    b -= 2
    if a == 1:
        if ltate[b] == 0:
            ans -= ta
        else:
            ans -= tate[b]

        for j in range(b, n - 2):
            if ltate[j] == 0:
                tate[j] = ta
                ltate[j] = 1
                yo = b
            else:
                break

    else:
        if lyoko[b] == 0:
            ans -= yo
        else:
            ans -= yoko[b]
        for j in range(b, n - 2):
            if lyoko[j] == 0:
                yoko[j] = yo
                lyoko[j] = 1
                ta = b
            else:
                break
print(ans)
