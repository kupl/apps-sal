n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))

next = a[0] - 1
b.append(next + 1)
for i in range(n):
    next = a[next] - 1
    b.append(next + 1)
print(b.index(2) + 1) if 2 in b else print(-1)
