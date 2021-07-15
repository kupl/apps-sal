import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())


n = inint()

wt = []

for i in range(n):
    a, b = inintm()
    wt.append([a,b])

wt = sorted(wt, reverse=True, key=lambda x: x[1])[::-1]

t = 0

for j in range(n):
    t += wt[j][0]
    if t > wt[j][1]:
        print("No")
        return

print("Yes")
