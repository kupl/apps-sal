import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n = ni()
a = na()
a = sorted(a)[::-1]
ans = sum(a[:(n+1)//2])*2-a[0]
ans = ans if n%2==0 else ans-a[(n+1)//2-1]

print(ans)

