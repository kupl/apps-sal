n = int(input())
d = {}
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
for i in range(n):
    d[a[i]] = i
c = d[b[0]]
print(c + 1, end=' ')
for i in range(1, n):
    if d[b[i]] < c:
        print(0, end=' ')
    else:
        print(d[b[i]] - c, end=' ')
        c = d[b[i]]
