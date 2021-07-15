(x1, y1) = input().split(" ")
x1 = int(x1)
y1 = int(y1)
(x2, y2) = input().split(" ")
x2 = int(x2)
y2 = int(y2)
n = int(input())
lineslist = []
for i in range(n):
    (a, b, c) = input().split(" ")
    lineslist.append((int(a), int(b), int(c)))

def greaterThanLine(x, y, a, b, c):
    return a*x + b*y + c > 0

count = 0
for line in lineslist:
    (a, b, c) = line
    if greaterThanLine(x1, y1, a, b, c) ^ greaterThanLine(x2, y2, a, b, c):
        count += 1

print(count)

