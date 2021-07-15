import sys
stdin = sys.stdin
sys.setrecursionlimit(10**9)

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()


n = ns()
n = list(map(int,n[::-1])) + [0]

ans = 0

for i in range(len(n)):
    a = n[i]
    if a <= 4:
        ans += a
    elif a >= 6:
        ans += 10-a
        n[i+1] += 1
    else:
        if n[i+1] <= 4:
            ans += a
        else:
            ans += a
            n[i+1] += 1

print(ans)
