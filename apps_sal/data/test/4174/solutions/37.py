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


n, x = LI()
l = LI()
cnt = 1
d = 0
for i in range(n):
    # print(f'{(d, l[i])=}')
    if d + l[i] <= x:
        cnt += 1
        d += l[i]
    else:
        break
print(cnt)
