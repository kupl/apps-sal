import sys
sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 10**9 + 7
def input(): return sys.stdin.readline().rstrip()
def YesNo(b): return bool([print('Yes')] if b else print('No'))
def YESNO(b): return bool([print('YES')] if b else print('NO'))


def int1(x): return int(x) - 1


N = int(input())
L = list(map(int, input().split()))
L.sort(reverse=1)
ans = 0
for i in range(N):
    ans += min(L[i * 2], L[i * 2 + 1])
print(ans)
