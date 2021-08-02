def isLeft(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) < 0


def isMn(s):
    return not (True in s and False in s)


def pr():
    for i in range(1, n - 1):
        s.append(isLeft(x[i - 1], y[i - 1], x[i], y[i], x[i + 1], y[i + 1]))
    s.append(isLeft(x[-1], y[-1], x[0], y[0], x[1], y[1]))
    s.append(isLeft(x[-2], y[-2], x[-1], y[-1], x[0], y[0]))


n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
s = []
pr()
ans = 0
for i in range(len(s)):
    if not s[i]:
        ans += 1
print(min(ans, len(s) - ans))
