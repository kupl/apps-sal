# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
import bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

n, k = list(map(int, input().split()))
k -= 1
a = [-1 for i in range(n)]
c = 1


def merge(l, r, k):
    nonlocal a, c
    if l >= r or k % 2 != 0:
        return False
    if k == 0:
        for i in range(l, r):
            a[i] = c
            c += 1
        return True
    k -= 2
    m = (l + r) // 2
    if (k // 2) % 2 == 0:
        if merge(m, r, k // 2):
            return merge(l, m, k // 2)
        else:
            return False
    else:
        if merge(m, r, k // 2 + 1):
            return merge(l, m, k // 2 - 1)
        else:
            return False


if not merge(0, n, k):
    print(-1)
    return
print(*a)
