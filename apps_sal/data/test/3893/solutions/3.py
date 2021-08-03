line = input().split()
x1 = int(line[0])
y1 = int(line[1])
line = input().split()
x2 = int(line[0])
y2 = int(line[1])
n = int(input())
ans = 0
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    d1 = (a * x1 + b * y1 + c)
    d2 = (a * x2 + b * y2 + c)
    if d1 * d2 < 0:
        ans += 1

print(ans)
