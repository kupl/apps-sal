import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))
def nn(): return list(stdin.readline().split())
def ns(): return stdin.readline().rstrip()


n = ni()
a = 2
ans = ''

if n == 0:
    print(0)
    return

while n != 0:
    if n % a == 0:
        ans = '0' + ans
    else:
        ans = '1' + ans
        n -= (a // 2)
    a *= (-2)

print(ans)
