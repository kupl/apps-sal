import math
n = int(input())
s = input()
c = list(map(int, input().split()))
h = [0] * n
ta = 0
tr = 0
td = 0
for i in range(n):
    if s[i] == 'h':
        h[i] = c[i]
    if i:
        h[i] = h[i] + h[i - 1]
    if s[i] == 'a':
        ta = min(ta + c[i], h[i])
    elif s[i] == 'r':
        tr = min(tr + c[i], ta)
    elif s[i] == 'd':
        td = min(td + c[i], tr)
print(td)
