import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
P = inintl()

ans = 0

for i in range(n-1):
    a = P[i]
    b = P[i+1]
    if a == i+1:
        P[i] = b
        P[i+1] = a
        ans += 1

if P[-1] == n:
    ans += 1

print(ans)
