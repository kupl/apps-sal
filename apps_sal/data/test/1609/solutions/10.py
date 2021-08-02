import sys


n = int(input())
x = str(input()).split()
a = {a: 1 for a in range(1, n + 1)}
c = []

for i in range(n):
    if int(x[i]) > n:
        c.append(i)
        continue
    if a.get(int(x[i])) == 1:
        a.pop(int(x[i]))
        continue
    else:
        c.append(i)

for i in range(len(c)):
    x[c[i]] = a.popitem()[0]

for i in range(n - 1):
    print(x[i], end=" ")
print(x[n - 1])
