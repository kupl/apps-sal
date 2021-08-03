import sys
from math import gcd


def osa_k(sieve, MAXN):
    p = 2
    while p * p <= MAXN:
        # まだチェックされていないなら
        if sieve[p] == p:
            # 次のqの倍数からp刻みでチェック入れていく
            for q in range(2 * p, MAXN + 1, p):
                if sieve[q] == q:
                    sieve[q] = p
        p += 1


def input(): return sys.stdin.readline().rstrip()


n = int(input())
A = list(map(int, input().split()))
nowgcd = A[0]
# 全体のGCDを取る
for i in A:
    nowgcd = gcd(nowgcd, i)
if nowgcd != 1:
    print('not coprime')
    return

MAXN = 10**6 + 5
sieve = [i for i in range(MAXN + 1)]
p = 2
osa_k(sieve, MAXN)

check = set()
for a in A:
    tmp = set()
    while (a > 1):
        tmp.add(sieve[a])
        a //= sieve[a]
    for p in tmp:
        if p in check:
            print('setwise coprime')
            return
        check.add(p)
print('pairwise coprime')
