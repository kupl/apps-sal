import sys
n, m, k = map(int, input().split())
a = [int(i) - 1 for i in input().split()]
b = [0] * n
for i in a:
    b[i] = 1
now = 0
for i in range(k):
    if b[now]:
        print(now + 1)
        return
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if now == x:
        now = y
    elif now == y:
        now = x

print(now + 1)
