n = int(input())
d = {1: 0}
j = 2
for i in map(int, input().split()):
    d[j] = i
    j += 1
a = [n]
while d[n] != 0:
    a.append(d[n])
    n = d[n]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=' ')
