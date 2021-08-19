import sys


def input():
    return sys.stdin.readline().strip()


(n, m) = [int(x) for x in input().split()]
can = [True for i in range(n + 1)]
for i in range(m):
    ai = int(input())
    can[ai] = False
C = [0 for i in range(n + 1)]
for i in range(n + 1):
    if i == 0:
        C[i] = 1
    else:
        C[i] = sum((C[j] if j >= 0 and can[j] else 0 for j in (i - 1, i - 2))) % (10 ** 9 + 7)
print(C[n])
