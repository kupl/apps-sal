n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
d = l[::]
l.sort()
d.sort(reverse=True)
print(sum((l[x] * d[x] for x in range(n))) % 10007)
