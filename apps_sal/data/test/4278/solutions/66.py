import sys
import math


def inint(): return int(sys.stdin.readline())
def inintm(): return map(int, sys.stdin.readline().split())
def inintl(): return list(inintm())
def instrm(): return map(str, sys.stdin.readline().split())
def instrl(): return list(instrm())


n = inint()

z = {(): 0}
ans = 0


def combinations(n, r):
    if n < r:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


for i in range(n):
    c = [0] * 123
    s = input()
    for j in range(len(s)):
        c[ord(s[j])] += 1
    try:
        z[tuple(c)] += 1
    except:
        z[tuple(c)] = 1

for i in z:
    ans += combinations(z[i], 2)

print(ans)
