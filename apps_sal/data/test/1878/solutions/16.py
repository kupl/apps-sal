n = int(input())
a = []
for i in range(100):
    a.append([])
    for j in range(100):
        a[i].append(0)
for i in range(n):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    for t in range(x1-1, x2):
        for k in range(y1-1, y2):
            a[t][k] += 1
num = 0
for i in range(100):
    num += sum(a[i])
print(num)
