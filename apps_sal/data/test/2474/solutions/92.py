import sys
import itertools
import fractions
stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


N = int(input())
C = nl()
mod = 10**9 + 7
n = 0
C.sort()
two = [0] * (N + 1)
two[0] = 1
for i in range(N):
    two[i + 1] = (two[i] * 2) % mod
ans = 0
for i in range(N):
    l = i
    r = N - 1 - i
    now = two[r]
    if(r != 0):
        now += two[r - 1] * r
    now *= two[i]
    now *= C[i]
    ans += now
    ans %= mod

ans *= two[N]
print((ans % mod))
