import sys


def inint(): return int(sys.stdin.readline())
def inintm(): return map(int, sys.stdin.readline().split())
def inintl(): return list(inintm())
def instrm(): return map(str, sys.stdin.readline().split())
def instrl(): return list(instrm())


n = inint()
P = inintl()

ans = 0

for i in range(n - 1):
    a = P[i]
    b = P[i + 1]
    if a == i + 1:
        P[i] = b
        P[i + 1] = a
        ans += 1

if P[-1] == n:
    ans += 1

print(ans)
