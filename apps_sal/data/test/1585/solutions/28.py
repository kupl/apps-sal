import sys


def IN_I(): return int(sys.stdin.readline().rstrip())
def IN_LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IN_LF(): return list(map(float, sys.stdin.readline().rstrip().split()))
def IN_S(): return sys.stdin.readline().rstrip()
def IN_LS(): return list(sys.stdin.readline().rstrip().split())


INF = float('inf')
MOD = 10**9 + 7


X, Y = IN_LI()

ans = 0
while X <= Y:
    ans += 1
    X = X * 2

print(ans)
