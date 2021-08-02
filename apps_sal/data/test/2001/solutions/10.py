import sys


def numIN():
    return(map(int, sys.stdin.readline().strip().split()))


MOD = 10**9 + 7

n, q = numIN()
l = [int(i) for i in input()]
pre = []
s = 0
for i in l:
    s += i
    pre.append(s)
for i in range(q):
    l, r = numIN()
    l -= 1
    r -= 1
    if l != 0:
        one = pre[r] - pre[l - 1]
        zero = r - l + 1 - one
        x = pow(2, one, MOD) - 1
        y = pow(2, zero, MOD)
        ans = x * y
        ans %= MOD
        print(ans)
    else:
        one = pre[r]
        zero = r - l + 1 - one
        x = pow(2, one, MOD) - 1
        y = pow(2, zero, MOD)
        ans = x * y
        ans %= MOD
        print(ans)
