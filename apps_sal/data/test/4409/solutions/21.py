n = int(input())
a = list(map(int, input().split()))
d = {}
for c in a:
    d[c] = d.get(c, 0) + 1
km = a[0]
for c in d:
    if d[c] > d[km]:
        km = c
pos = 0
for i in range(n):
    if a[i] == km:
        pos = i
        break
print(n - d[km])
for i in range(pos + 1, n):
    if a[i] > km:
        print(2, i + 1, i)
    elif a[i] < km:
        print(1, i + 1, i)
for i in range(pos - 1, -1, -1):
    if a[i] > km:
        print(2, i + 1, i + 2)
    elif a[i] < km:
        print(1, i + 1, i + 2)
