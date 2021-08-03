import sys
n, x = map(int, input().split())
m = [int(input()) for i in range(n)]

a = sum(m)
b = min(m)

k = x - a
c = k // b + n

print(c)
