import sys

#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())


def sign(a, b, c, x, y):
    value = a * x + b * y + c
    if value < 0:
        return -1
    if value == 0:
        return 0
    return 1


n, ans = int(input()), 0
for i in range(n):
    a, b, c = map(int, input().split())
    if sign(a, b, c, x1, y1) != sign(a, b, c, x2, y2):
        ans += 1
print(ans)
