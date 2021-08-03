import math

n = int(input())
ta = [list(map(int, input().split())) for _ in range(n)]

x, y = ta[0]
for i in range(1, n):
    t, a = ta[i]
    k = max(-(-x // t), -(-y // a))
    x, y = k * t, k * a

print((x + y))
