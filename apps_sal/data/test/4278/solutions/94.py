import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()

z = {}
ans = 0

for i in range(n):
    s = "".join(sorted(input()))
    try:
        z[s] += 1
    except:
        z[s] = 1

for i in z:
    ans += z[i]*(z[i]-1)//2

print(ans)
