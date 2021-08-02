a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(input())
d = []
for i in range(c):
    d += [list(map(int, input().split()))]
e = list([j[0] * a[0] + j[1] * a[1] + j[2] > 0 for j in d])
f = list([j[0] * b[0] + j[1] * b[1] + j[2] > 0 for j in d])
print(len(list([x for x in range(len(d)) if e[x] != f[x]])))
