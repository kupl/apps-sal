n, m = map(int, input().split())
a = list(map(int, input().split()))
d = {}
for i in range(m):
    d[i] = []
for i in range(len(a)):
    r = a[i] % m
    d[r].append((a[i], i))
# print(d)
step = 0
x = n // m
stack = []
# print(d)
for i in range(2 * m):
    i = i % m
    # print(i,stack)
    while(len(d[i]) > x):
        stack.append(d[i].pop())
    while(len(d[i]) < x and len(stack)):
        z = list(stack.pop())
        delta = (i + m - (z[0] % m)) % m
        z[0] += delta
        d[i].append((z[0], z[1]))
        step += delta
arr = []
# print(d)
for i in d:
    for j in d[i]:
        arr.append(j)
arr.sort(key=lambda i: i[1])
print(step)
for i in arr:
    print(i[0], end=" ")
print()
