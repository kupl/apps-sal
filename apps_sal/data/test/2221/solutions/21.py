x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
n = int(input())
S = input()

xw = 0
yw = 0
WALKLIST = [(0, 0)]
for s in S:
    if s == "U":
        yw += 1
    elif s == "D":
        yw -= 1
    elif s == "L":
        xw -= 1
    elif s == "R":
        xw += 1
    WALKLIST.append((xw, yw))

MIN = 0
MAX = 10**15

while MIN != MAX:
    x = (MIN + MAX) // 2

    r, d = divmod(x, n)
    if abs(x2 - (x1 + r * xw + WALKLIST[d][0])) + abs(y2 - (y1 + r * yw + WALKLIST[d][1])) <= x:
        MAX = x
    else:
        MIN = x + 1

    if MIN == 10**15:
        print(-1)
        break
else:
    print(MAX)
