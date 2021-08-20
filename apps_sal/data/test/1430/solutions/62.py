from itertools import groupby
(n, k) = map(int, input().split())
s = input()
L = []
for (key, value) in groupby(s):
    L.append((key, len(list(value))))
c = []
for i in range(len(L)):
    c.append(L[i][1])
c = [0] + c
for i in range(1, len(c)):
    c[i] += c[i - 1]
l = 0
r = 2 * k
ans = 0
while True:
    if L[l][0] == '1':
        if l + r + 1 < len(L):
            ans = max(ans, c[l + r + 1] - c[l])
        else:
            ans = max(ans, c[len(L)] - c[l])
    elif L[l][0] == '0':
        if l + r < len(L):
            ans = max(ans, c[l + r] - c[l])
        else:
            ans = max(ans, c[len(L)] - c[l])
    if l == len(L) - 1:
        break
    l += 1
print(ans)
