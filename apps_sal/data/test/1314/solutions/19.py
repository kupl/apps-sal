from collections import Counter


def mi():
    return list(map(int, input().split()))


'\n2\n2 5\n-6 4\n7 -2\n-1 -3\n'
n = int(input())
c = [0] * n
for i in range(n):
    c[i] = list(mi())
d = [0] * n
for i in range(n):
    d[i] = list(mi())
possans = [0] * (n * n)
k = 0
for i in range(n):
    for j in range(n):
        t1 = (c[i][0] + d[j][0], c[i][1] + d[j][1])
        possans[k] = t1
        k += 1
c = Counter(possans)
c = sorted(c, key=c.get)
print(*c[-1])
