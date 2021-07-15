import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
a = 2
ans = ''

if n==0:
    print(0)
    return

while n != 0:
    if n%a == 0:
        ans = '0' + ans
    else:
        ans = '1' + ans
        n-=(a//2)
    a*=(-2)

print(ans)
