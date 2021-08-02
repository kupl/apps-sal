import sys
n, m, x = map(int, input().split())
a = list(map(int, input().split()))

s = 0
b = 0
for i in a:
    if i < x:
        s += 1
    if i > x:
        b += 1
print(min(s, b))
