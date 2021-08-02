from random import randrange
from collections import Counter
import sys
INF = 1 << 60
MOD = 10**9 + 7  # 998244353
sys.setrecursionlimit(2147483647)
input = lambda: sys.stdin.readline().rstrip()


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if Counter(A + B).most_common()[0][1] > n:
        print("No")
        return

    for i in range(n):
        if A[i] != B[i]:
            continue
        while 1:
            j = randrange(0, n)
            if A[i] != B[j] and A[j] != B[i]:
                B[i], B[j] = B[j], B[i]
                break
    print("Yes")
    print(*B)


resolve()
