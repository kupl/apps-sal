# from debug import debug
import sys

# t = int(input())
# for _ in range(t):
# n = inputt(input())
# s = input()
n, k = list(map(int, input().split()))
lis = list(map(int, input().split()))

v = [0] * (n + 2)
p = [0] * (n + 2)
c = [0] * n
# lis.reverse()
for i in lis:
    i -= 1
    c[i] = 1
    if i + 1 < n and c[i + 1] == 1:
        v[i + 1] = 1
    if i - 1 >= 0 and c[i - 1] == 1:
        p[i - 1] = 1

x = 0
for i in lis:
    i -= 1
    if c[i]:
        x += c[i] + v[i] + p[i]
    else:
        if i + 1 < n:
            x += c[i + 1]
        if i - 1 >= 0:
            x += c[i - 1]
# debug(v=v, p=p, c=c)
x = 0
for i in range(0, n):
    x += c[i] + v[i + 1] + p[i - 1]
# print(x)
print(3 * n - 2 - x)
