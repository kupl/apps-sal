from sys import stdin, stdout


x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
x5, y5, x6, y6 = list(map(int, input().split()))


S1 = 0
S2 = 0
S = 0

l1 = min(x2, x4) - max(x1, x3)
h1 = min(y2, y4) - max(y1, y3)

if l1 >= 0 and h1 >= 0:
    S1 = l1 * h1

l2 = min(x2, x6) - max(x1, x5)
h2 = min(y2, y6) - max(y1, y5)

if l2 >= 0 and h2 >= 0:
    S2 = l2 * h2

l3 = min(x2, x6, x4) - max(x1, x5, x3)
h3 = min(y2, y6, y4) - max(y1, y5, y3)

if l3 >= 0 and h3 >= 0:
    S = l3 * h3

if S1 + S2 - S == (x2 - x1) * (y2 - y1):
    print("NO")
else:
    print("YES")
