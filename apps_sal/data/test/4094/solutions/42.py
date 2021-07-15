import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


k = I()
ans = -1
a = [0] * (k+1)
a[1] = 7 % k
for i in range(2, k+1):
    a[i] = (a[i-1]*10 + 7) % k

for i in range(1, k+1):
    if a[i] == 0:
        print(i)
        return
print((-1))

