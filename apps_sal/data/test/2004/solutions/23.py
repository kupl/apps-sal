n = int(input())
n += 1
a = []
for i in range(2, n, 2):
    a.append(i)
a.append(1)
for j in range(2, n, 2):
    if j + 1 < n:
        a.append(j + 1)
    a.append(j)
print(len(a))
for x in a:
    print(x, end=' ')
