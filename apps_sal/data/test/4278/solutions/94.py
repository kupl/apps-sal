import sys
import math


def inint(): return int(sys.stdin.readline())
def inintm(): return map(int, sys.stdin.readline().split())
def inintl(): return list(inintm())
def instrm(): return map(str, sys.stdin.readline().split())
def instrl(): return list(instrm())


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
    ans += z[i] * (z[i] - 1) // 2

print(ans)
