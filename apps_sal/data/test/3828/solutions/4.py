__author__ = 'Utena'
n = int(input())
m = list(map(int, input().split()))
t = 0
l = [0]
r = [0] * (n + 1)
for j in range(n):
    r[m[j]] = j + 1
if n == 1:
    print(0)
else:
    for i in range(1, n):
        t += 1
        if r[i] > r[i + 1]:
            l.append(t)
            t = 0
    if r[n] > r[n - 1]:
        t += 1
        l.append(t)
    print(n - max(l))
