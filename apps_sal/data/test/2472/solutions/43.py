import sys


def inint(): return int(sys.stdin.readline())
def inintm(): return map(int, sys.stdin.readline().split())
def inintl(): return list(inintm())
def instrm(): return map(str, sys.stdin.readline().split())
def instrl(): return list(instrm())


n = inint()

wt = []

for i in range(n):
    a, b = inintm()
    wt.append([a, b])

wt = sorted(wt, reverse=True, key=lambda x: x[1])[::-1]

t = 0

for j in range(n):
    t += wt[j][0]
    if t > wt[j][1]:
        print("No")
        return

print("Yes")
