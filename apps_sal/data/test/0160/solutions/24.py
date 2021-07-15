def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    table = list(table)
    return table

def binary_search_int(ok, ng, test):
    """
    :param ok: solve(x) = True を必ず満たす点
    :param ng: solve(x) = False を必ず満たす点
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if test(mid):
            ok = mid
        else:
            ng = mid
    return ok

import numpy as np
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))
S = sum(A)
D = divisors(S)
D.sort()

def test(x):
    k = D[x]
    B = A%k
    B.sort()
    cnt = sum(B)//k
    return k*cnt - sum(B[-cnt:]) <= K

p = binary_search_int(0,len(D),test)
q = binary_search_int(p+1,len(D),test)
print(max(D[p],D[q]) if q != p+1 else D[p])
