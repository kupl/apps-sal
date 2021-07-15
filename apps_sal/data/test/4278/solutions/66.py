import sys
import math


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()

z = {():0}
ans = 0

def combinations(n, r):
    if n < r:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for i in range(n):
    c = [0]*123
    s = input()
    for j in range(len(s)):
        c[ord(s[j])] += 1
    try:
        z[tuple(c)] += 1
    except:
        z[tuple(c)] = 1

for i in z:
    ans += combinations(z[i],2)

print(ans)
